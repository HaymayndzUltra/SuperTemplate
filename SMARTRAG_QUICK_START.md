# SmartRag Integration Quick Start Guide

**For:** SuperTemplate System Engineers  
**Goal:** Get SmartRag MCP server integrated with minimal disruption  
**Time:** 1-2 weeks for POC, 4-8 weeks for production

---

## TL;DR

SmartRag adds **web crawling, RAG, and code validation** to SuperTemplate workflows. Best used for:
- ✅ Crawling framework documentation during bootstrap (Protocol 04)
- ✅ Enriching proposals with competitor research (Protocol 01)
- ✅ Validating generated code against knowledge graphs (Protocol 10, 23)

**Key Decision:** Use as **optional enhancement layer**, NOT core dependency.

---

## Prerequisites

```bash
# 1. Install SmartRag dependencies
cd /path/to/smartrag
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# 2. Set up environment
cp .env.example .env
# Edit .env:
# - OPENAI_API_KEY (required for embeddings)
# - SUPABASE_URL + SUPABASE_SERVICE_KEY (required for vector DB)
# - NEO4J_URI (optional, for knowledge graph)

# 3. Test MCP server
uv run crawl4ai_mcp
```

---

## Integration Pattern: Service Layer

```
SuperTemplate Orchestrator
        │
        ├─ Quality Gates (existing)
        │
        └─ SmartRag Service ← NEW
                │
                ├─ MCP Client
                ├─ Cache Layer (Redis)
                └─ Fallback Logic
```

**Why This Pattern:**
- ✅ Protocol independence preserved
- ✅ Graceful degradation if SmartRag unavailable
- ✅ Easy to disable (single config flag)

---

## Quick Win #1: Protocol 04 Documentation Crawler (1-2 hours)

### Goal
Auto-crawl framework documentation during project bootstrap.

### Implementation

**Step 1:** Create SmartRag service wrapper

```python
# scripts/smartrag_service.py
import asyncio
import json
from typing import Dict, Any, Optional
from pathlib import Path

class SmartRagService:
    """Lightweight wrapper for SmartRag MCP calls."""
    
    def __init__(self, mcp_command: list[str], cache_dir: Path):
        self.mcp_command = mcp_command
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    async def crawl_documentation(self, url: str, framework: str) -> Dict[str, Any]:
        """Crawl documentation with caching."""
        cache_file = self.cache_dir / f"{framework}.json"
        
        # Check cache (24h TTL)
        if cache_file.exists():
            mtime = cache_file.stat().st_mtime
            if time.time() - mtime < 86400:  # 24 hours
                return json.loads(cache_file.read_text())
        
        # Call MCP server
        process = await asyncio.create_subprocess_exec(
            *self.mcp_command,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "smart_crawl_url",
                "arguments": {"url": url, "max_depth": 2}
            }
        }
        
        stdout, stderr = await process.communicate(json.dumps(request).encode())
        result = json.loads(stdout.decode())
        
        # Cache result
        cache_file.write_text(json.dumps(result["result"]))
        return result["result"]
```

**Step 2:** Integrate with Protocol 04

```python
# scripts/bootstrap_project.py (ADD to existing file)

# ... existing imports ...
from scripts.smartrag_service import SmartRagService

async def crawl_framework_docs(technical_baseline: Dict[str, Any], config: Dict[str, Any]):
    """Crawl framework documentation during bootstrap."""
    
    # Check if SmartRag enabled in config
    if not config.get("smartrag", {}).get("enabled", False):
        print("ℹ️  SmartRag disabled, skipping documentation crawl")
        return {}
    
    try:
        smartrag = SmartRagService(
            mcp_command=["uv", "run", "crawl4ai_mcp"],
            cache_dir=Path(".artifacts/smartrag-cache")
        )
        
        docs = {}
        for framework in technical_baseline["stack"].values():
            print(f"📚 Crawling {framework} documentation...")
            try:
                docs[framework] = await smartrag.crawl_documentation(
                    url=f"https://docs.{framework.lower()}.com",
                    framework=framework
                )
                print(f"✓ {framework} documentation cached")
            except Exception as e:
                print(f"✗ Failed to crawl {framework}: {e}")
                # Non-blocking: continue even if crawl fails
                
        # Store manifest
        manifest_path = Path(".artifacts/protocol-04/smartrag-docs-manifest.json")
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps({
            "sources": docs,
            "timestamp": datetime.now().isoformat()
        }, indent=2))
        
        return docs
        
    except Exception as e:
        print(f"⚠️  SmartRag service unavailable: {e}")
        print("   Continuing with standard bootstrap...")
        return {}

# ... existing bootstrap_project() function ...
# ADD this call after technical baseline extraction:
if __name__ == "__main__":
    # ... existing arg parsing ...
    
    technical_baseline = extract_technical_baseline(project_brief)
    
    # NEW: Crawl docs asynchronously
    docs = asyncio.run(crawl_framework_docs(technical_baseline, config))
    
    # ... continue with existing bootstrap logic ...
```

**Step 3:** Add configuration

```yaml
# config.yaml (or plano.yaml)
smartrag:
  enabled: true  # Set to false to disable
  cache_ttl: 86400  # 24 hours
  mcp_server:
    command: ["uv", "run", "crawl4ai_mcp"]
```

**Step 4:** Test

```bash
# Run bootstrap with SmartRag enabled
python scripts/bootstrap_project.py \
  --brief PROJECT-BRIEF.md \
  --config config.yaml

# Expected output:
# 📚 Crawling react documentation...
# ✓ react documentation cached
# 📚 Crawling fastapi documentation...
# ✓ fastapi documentation cached
```

**Result:** Framework docs cached in `.artifacts/smartrag-cache/` for AI context loading.

---

## Quick Win #2: Protocol 01 Competitor Research (2-4 hours)

### Goal
Enrich job post analysis with crawled competitor solutions.

### Implementation

```python
# scripts/aggregate_evidence_01.py (ADD function)

async def research_competitors(jobpost_analysis: Dict[str, Any], config: Dict[str, Any]):
    """Research competitor solutions mentioned in job post."""
    
    if not config.get("smartrag", {}).get("enabled", False):
        return {}
        
    try:
        smartrag = SmartRagService(
            mcp_command=["uv", "run", "crawl4ai_mcp"],
            cache_dir=Path(".artifacts/smartrag-cache")
        )
        
        research = {}
        
        # Extract competitor URLs from job post
        competitors = jobpost_analysis.get("competitor_references", [])
        
        for comp in competitors:
            print(f"🔍 Researching {comp['name']}...")
            try:
                result = await smartrag.crawl_documentation(
                    url=comp["url"],
                    framework=comp["name"]
                )
                research[comp["name"]] = {
                    "features": extract_features(result),
                    "pricing": extract_pricing(result),
                    "tech_stack": extract_tech_stack(result)
                }
                print(f"✓ {comp['name']} analysis complete")
            except Exception as e:
                print(f"✗ Failed to research {comp['name']}: {e}")
                
        return research
        
    except Exception as e:
        print(f"⚠️  SmartRag unavailable: {e}")
        return {}

# ADD to main() function:
if __name__ == "__main__":
    # ... existing code ...
    
    # NEW: Add competitor research
    if jobpost_analysis.get("competitor_references"):
        competitor_research = asyncio.run(
            research_competitors(jobpost_analysis, config)
        )
        jobpost_analysis["external_research"] = competitor_research
    
    # ... continue with existing logic ...
```

**Result:** Proposals enriched with competitive intelligence.

---

## Quick Win #3: Protocol 10 Code Validation (4-6 hours)

### Goal
Validate generated Python code against knowledge graph to catch hallucinations.

### Prerequisites
- Neo4j running (Docker: `docker run -p 7687:7687 neo4j`)
- `USE_KNOWLEDGE_GRAPH=true` in SmartRag `.env`

### Implementation

```python
# scripts/lane_executor.py (ADD function)

async def validate_generated_code(
    task: Dict[str, Any],
    generated_code: str,
    config: Dict[str, Any]
) -> Dict[str, Any]:
    """Validate generated code against knowledge graph."""
    
    if not config.get("smartrag", {}).get("knowledge_graph", False):
        return {"validated": False, "reason": "Knowledge graph disabled"}
        
    if task["language"] != "python":
        return {"validated": False, "reason": "Only Python validation supported"}
        
    try:
        smartrag = SmartRagService(
            mcp_command=["uv", "run", "crawl4ai_mcp"],
            cache_dir=Path(".artifacts/smartrag-cache")
        )
        
        # Call hallucination detection tool
        process = await asyncio.create_subprocess_exec(
            *smartrag.mcp_command,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE
        )
        
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "check_ai_script_hallucinations",
                "arguments": {"script_content": generated_code}
            }
        }
        
        stdout, _ = await process.communicate(json.dumps(request).encode())
        result = json.loads(stdout.decode())
        
        validation = result["result"]
        
        if validation.get("hallucinations_found", False):
            print(f"⚠️  Hallucinations detected in {task['id']}:")
            for issue in validation.get("issues", []):
                print(f"   - {issue['type']}: {issue['message']}")
                
        return validation
        
    except Exception as e:
        print(f"⚠️  Code validation failed: {e}")
        return {"validated": False, "error": str(e)}

# MODIFY execute_task() function:
async def execute_task(task: Dict[str, Any], config: Dict[str, Any]):
    # ... existing task execution logic ...
    
    generated_code = result["code"]
    
    # NEW: Validate code
    validation = await validate_generated_code(task, generated_code, config)
    
    if validation.get("hallucinations_found"):
        # Log for human review
        log_validation_failure(task["id"], validation)
        
        # Optionally block task completion
        if config.get("smartrag", {}).get("block_on_hallucinations", False):
            raise ValidationError(f"Hallucinations detected: {validation['issues']}")
    
    result["validation"] = validation
    return result
```

**Result:** AI-generated code validated against repository structure before gate checks.

---

## Configuration Reference

```yaml
# plano.yaml or config.yaml
smartrag:
  # Master toggle - set to false to disable ALL SmartRag features
  enabled: true
  
  # Cache configuration
  cache_ttl: 86400  # 24 hours in seconds
  cache_dir: ".artifacts/smartrag-cache"
  
  # MCP server configuration
  mcp_server:
    command: ["uv", "run", "crawl4ai_mcp"]
    working_dir: "/path/to/smartrag"  # Optional, defaults to smartrag repo location
    
  # RAG strategies (map to SmartRag .env variables)
  strategies:
    hybrid_search: true       # USE_HYBRID_SEARCH
    agentic_rag: true         # USE_AGENTIC_RAG (code examples)
    reranking: true           # USE_RERANKING
    contextual_embeddings: false  # USE_CONTEXTUAL_EMBEDDINGS (expensive)
    
  # Knowledge graph features (requires Neo4j)
  knowledge_graph:
    enabled: false  # Set to true if Neo4j is available
    block_on_hallucinations: false  # Set to true to fail tasks on validation errors
    
  # Protocol-specific toggles (can disable per-protocol)
  protocols:
    "01": true  # Competitor research in proposals
    "04": true  # Documentation crawling in bootstrap
    "07": true  # Architecture pattern research
    "10": true  # Code validation during task execution
    "12": true  # Security vulnerability lookup in audit
    "19": true  # Documentation reference enrichment
    "23": true  # Script governance validation
```

---

## Troubleshooting

### Issue: "SmartRag MCP server not responding"

```bash
# Check MCP server status
uv run crawl4ai_mcp --help

# Test MCP server manually
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | uv run crawl4ai_mcp

# Check environment variables
grep -E "OPENAI_API_KEY|SUPABASE" .env
```

### Issue: "Supabase authentication failed"

```bash
# Verify Supabase credentials
curl -X GET "https://YOUR_PROJECT.supabase.co/rest/v1/" \
  -H "apikey: YOUR_SERVICE_KEY"
  
# Re-initialize Supabase tables
python knowledge_graphs/init_supabase.py
```

### Issue: "Neo4j connection timeout"

```bash
# Check Neo4j status
docker ps | grep neo4j

# Restart Neo4j
docker restart neo4j

# Test connection
cypher-shell -u neo4j -p YOUR_PASSWORD "RETURN 'connected'"
```

### Issue: "High OpenAI API costs"

**Solution:** Adjust cache TTL and enable cache-first strategy

```yaml
smartrag:
  cache_ttl: 604800  # 7 days instead of 1 day
  cache_strategy: "aggressive"  # Cache everything
  
  # Disable expensive strategies
  strategies:
    contextual_embeddings: false  # Most expensive
    reranking: false              # Moderate cost
```

---

## Monitoring

### Add Metrics to Evidence Manager

```python
# scripts/evidence_manager.py (ADD method)

def log_smartrag_metrics(self, protocol: str, metrics: Dict[str, Any]):
    """Log SmartRag performance metrics."""
    self.log_execution(
        phase=self._protocol_to_phase(protocol),
        action="SmartRag Metrics",
        status="completed",
        details={
            "cache_hits": metrics.get("cache_hits", 0),
            "cache_misses": metrics.get("cache_misses", 0),
            "api_calls": metrics.get("api_calls", 0),
            "avg_latency_ms": metrics.get("avg_latency_ms", 0),
            "total_cost_usd": metrics.get("total_cost_usd", 0)
        }
    )
```

### View Metrics

```bash
# Generate SmartRag metrics report
python scripts/evidence_report.py --project demo --filter "SmartRag Metrics"

# Example output:
# SmartRag Metrics Summary:
#   Cache Hit Rate: 73% (22/30)
#   Avg Latency: 1,234 ms
#   Total API Calls: 8
#   Estimated Cost: $0.47
```

---

## Testing

### Unit Tests

```python
# tests/test_smartrag_service.py
import pytest
from scripts.smartrag_service import SmartRagService

@pytest.mark.asyncio
async def test_crawl_documentation_with_cache():
    service = SmartRagService(
        mcp_command=["uv", "run", "crawl4ai_mcp"],
        cache_dir=Path("/tmp/test-cache")
    )
    
    # First call - cache miss
    result1 = await service.crawl_documentation(
        url="https://docs.python.org",
        framework="python"
    )
    assert result1["status"] == "success"
    
    # Second call - cache hit
    result2 = await service.crawl_documentation(
        url="https://docs.python.org",
        framework="python"
    )
    assert result2 == result1
    assert result2["cache_hit"] == True

@pytest.mark.asyncio
async def test_graceful_degradation_when_unavailable():
    # Simulate MCP server unavailable
    service = SmartRagService(
        mcp_command=["nonexistent-command"],
        cache_dir=Path("/tmp/test-cache")
    )
    
    # Should not raise exception
    result = await service.crawl_documentation(
        url="https://docs.python.org",
        framework="python",
        fallback_enabled=True
    )
    
    assert result["status"] == "fallback"
    assert "error" in result
```

### Integration Tests

```bash
# Test Protocol 04 integration
python scripts/bootstrap_project.py \
  --brief tests/fixtures/test-brief.md \
  --config tests/fixtures/smartrag-enabled.yaml \
  --dry-run

# Expected: No errors, docs cached in .artifacts/smartrag-cache/
```

---

## Rollback Plan

If SmartRag causes issues:

```yaml
# Option 1: Disable globally
smartrag:
  enabled: false

# Option 2: Disable per-protocol
smartrag:
  enabled: true
  protocols:
    "01": false  # Disable only for Protocol 01
    "04": false
    # ... etc
```

```bash
# Clear cache
rm -rf .artifacts/smartrag-cache/

# Verify no hard dependencies
grep -r "smartrag" scripts/ | grep -v "if.*smartrag"
# Should only show conditional checks, no hard dependencies
```

---

## Next Steps

1. **POC (Week 1):**
   - Implement Quick Win #1 (Protocol 04)
   - Test with 3 real projects
   - Measure quality improvement

2. **Validation (Week 2):**
   - Implement Quick Win #2 (Protocol 01)
   - Run A/B test: 10 proposals with/without SmartRag
   - Calculate ROI

3. **Decision Gate:**
   - If >30% quality improvement → proceed to production
   - If <20% quality improvement → pause and reassess

4. **Production Rollout (Weeks 3-8):**
   - Follow phased rollout plan in main analysis doc
   - Add remaining protocol integrations
   - Implement monitoring and alerting

---

**Remember:** SmartRag should **enhance**, not **replace** existing workflows. Keep all integrations **optional** with **graceful degradation**.



