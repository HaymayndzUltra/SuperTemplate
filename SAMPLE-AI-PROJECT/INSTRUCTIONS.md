# 📋 HOW TO USE THIS SAMPLE

## Step 1: Copy to Your Repo

Copy the entire `SAMPLE-AI-PROJECT` folder to your target repository:

```bash
cp -r SAMPLE-AI-PROJECT/* /path/to/your/repo/
```

## Step 2: Make Sure You Have the Generate Cursor Rules Command

Ensure your repo has either:
- `.cursor/commands/generate-cursor-rules.md` OR
- `.cursor/ai-driven-workflow/00-generate-rules.md`

## Step 3: Run the Command

In Cursor, open chat and type:

```
/Generate Cursor Rules
```

Or with flags:

```
/Generate Cursor Rules --ai-ml-only
/Generate Cursor Rules --stack langchain --vector-db pinecone
/Generate Cursor Rules --dry-run
```

## Expected Output

The command will generate these files in `.cursor/rules/project-rules/`:

### Generated Rules:

1. **`nextjs-app-structure.mdc`**
   - Next.js 14 patterns
   - Component architecture
   - TypeScript conventions
   - Tailwind CSS guidelines

2. **`fastapi-backend-architecture.mdc`**
   - FastAPI patterns
   - Async/await best practices
   - API endpoint structure
   - Pydantic models

3. **`ai-ml-architecture.mdc`** ← NEW!
   - LangChain patterns
   - Prompt engineering guidelines
   - RAG pipeline implementation
   - Vector database integration
   - Agent workflow patterns

4. **`ai-testing-validation.mdc`** ← NEW!
   - LLM testing strategies
   - Prompt validation techniques
   - Embedding quality checks
   - Evaluation metrics
   - Mock LLM responses

5. **`database-patterns.mdc`** ← NEW!
   - Supabase integration
   - PostgreSQL best practices
   - Vector store patterns (Pinecone/ChromaDB)
   - Query optimization
   - Migration management

6. **`fullstack-integration-conventions.mdc`**
   - API contracts
   - Shared types between frontend/backend
   - Error handling patterns
   - Environment configuration
   - Local development setup

## What Each File Contains

### `ai-ml-architecture.mdc`
```markdown
- LangChain agent patterns
- Prompt template structures
- RAG pipeline implementation
- Vector database integration (Pinecone, ChromaDB, Weaviate)
- Embedding generation strategies
- Multi-agent orchestration
- Tool integration patterns
```

### `ai-testing-validation.mdc`
```markdown
- LLM output validation
- Prompt testing frameworks
- Mock LLM responses for testing
- Embedding quality metrics
- RAG pipeline testing
- Agent behavior testing
- Regression testing for prompts
```

### `database-patterns.mdc`
```markdown
- Supabase client setup
- PostgreSQL schema design
- Vector similarity search
- Pinecone index management
- ChromaDB collection patterns
- Query optimization
- Connection pooling
```

## Verification

After running the command, check:

```bash
ls -la .cursor/rules/project-rules/

# You should see:
# - nextjs-app-structure.mdc
# - fastapi-backend-architecture.mdc
# - ai-ml-architecture.mdc
# - ai-testing-validation.mdc
# - database-patterns.mdc
# - fullstack-integration-conventions.mdc
```

## Testing the Generated Rules

1. Open any `.ts` or `.tsx` file in your frontend code
2. The `nextjs-app-structure.mdc` rule should activate
3. Ask Cursor: "How should I structure a new component?"
4. It will follow the patterns from the generated rule

Similarly:
- Open `.py` files → `fastapi-backend-architecture.mdc` activates
- Work with LangChain → `ai-ml-architecture.mdc` activates
- Write tests → `ai-testing-validation.mdc` activates

## Customization

After generation, you can edit the `.mdc` files to:
- Add project-specific patterns
- Include actual code examples from your codebase
- Add team conventions
- Include links to internal documentation

## Troubleshooting

**If no rules are generated:**
1. Make sure the command file exists
2. Check that files like `package.json` and `requirements.txt` are in the root
3. Try with `--dry-run` first to see what would be generated

**If wrong rules are generated:**
1. Use flags like `--ai-ml-only` to be specific
2. Provide hints with `--stack langchain --vector-db pinecone`
3. Make sure `PROJECT-BRIEF.md` clearly describes the architecture

## Next Steps

After generation:
1. Review the generated rules
2. Customize them for your team
3. Add them to version control
4. Share with your team
5. Keep them updated as your codebase evolves


