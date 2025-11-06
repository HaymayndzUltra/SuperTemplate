# Protocol 21: AI Production Integration & API Development

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: mlops_deployment
phase: "Phase 5: MLOps & Deployment"
priority: critical
tags: [api-development, integration, rest-api, authentication, rate-limiting, documentation]
triggers: [api-integration, production-api, client-integration, sdk-generation]
```

## 1. Protocol Overview

**Purpose**: Develop production-ready REST APIs for ML model inference with authentication, rate limiting, request validation, comprehensive documentation, and client SDK generation for seamless integration.

**Critical Success Factors**:
- API security and authentication
- Request/response validation
- Rate limiting and throttling
- Comprehensive documentation
- Client SDK availability
- Performance optimization

## 2. API Development Workflow

### Step 1: API Design & Specification
**Duration**: 4-6 hours

**Activities**:
1. Define API endpoints
2. Design request/response schemas
3. Plan authentication strategy
4. Define rate limits
5. Create OpenAPI specification

**OpenAPI Specification**:
```yaml
# api/openapi-spec.yaml

openapi: 3.0.3
info:
  title: ML Model Inference API
  description: Production API for ML model predictions
  version: 1.0.0
  contact:
    name: ML Team
    email: ml-team@company.com
  license:
    name: Proprietary

servers:
  - url: https://api.company.com/v1
    description: Production server
  - url: https://staging-api.company.com/v1
    description: Staging server

security:
  - ApiKeyAuth: []
  - BearerAuth: []

paths:
  /predict:
    post:
      summary: Single prediction
      description: Make a single prediction using the ML model
      operationId: predict
      tags:
        - Predictions
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PredictionRequest'
            examples:
              fraud_detection:
                summary: Fraud detection example
                value:
                  features:
                    - 1500.50
                    - 2
                    - 0.75
                  metadata:
                    request_id: "req-123"
      responses:
        '200':
          description: Successful prediction
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PredictionResponse'
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
  
  /batch_predict:
    post:
      summary: Batch predictions
      description: Make multiple predictions in a single request
      operationId: batchPredict
      tags:
        - Predictions
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                requests:
                  type: array
                  items:
                    $ref: '#/components/schemas/PredictionRequest'
                  maxItems: 100
      responses:
        '200':
          description: Successful batch prediction
          content:
            application/json:
              schema:
                type: object
                properties:
                  predictions:
                    type: array
                    items:
                      $ref: '#/components/schemas/PredictionResponse'
  
  /health:
    get:
      summary: Health check
      description: Check API health status
      operationId: healthCheck
      tags:
        - Monitoring
      security: []
      responses:
        '200':
          description: API is healthy
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum: [healthy, degraded, unhealthy]
                  uptime_seconds:
                    type: number
                  model_loaded:
                    type: boolean

components:
  schemas:
    PredictionRequest:
      type: object
      required:
        - features
      properties:
        features:
          type: array
          items:
            type: number
          description: Input features for prediction
          minItems: 1
          maxItems: 1000
        metadata:
          type: object
          properties:
            request_id:
              type: string
            timestamp:
              type: string
              format: date-time
    
    PredictionResponse:
      type: object
      properties:
        prediction:
          type: number
          description: Model prediction
        probability:
          type: number
          minimum: 0
          maximum: 1
          description: Prediction confidence
        model_version:
          type: string
          description: Version of model used
        request_id:
          type: string
        processing_time_ms:
          type: number
    
    Error:
      type: object
      properties:
        error:
          type: string
        message:
          type: string
        request_id:
          type: string
        timestamp:
          type: string
          format: date-time

  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

### Step 2: FastAPI Implementation
**Duration**: 6-8 hours

**Complete FastAPI Application**:
```python
# api/main.py

from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict
import joblib
import numpy as np
import time
import logging
from datetime import datetime
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ML Model Inference API",
    description="Production API for ML model predictions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Global model variable
model = None
model_version = "1.0.0"

# Request/Response Models
class PredictionMetadata(BaseModel):
    request_id: Optional[str] = None
    timestamp: Optional[datetime] = None

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=1, max_items=1000)
    metadata: Optional[PredictionMetadata] = None
    
    @validator('features')
    def validate_features(cls, v):
        if any(np.isnan(x) or np.isinf(x) for x in v):
            raise ValueError("Features contain NaN or Inf values")
        return v

class PredictionResponse(BaseModel):
    prediction: float
    probability: float
    model_version: str
    request_id: str
    processing_time_ms: float

class BatchPredictionRequest(BaseModel):
    requests: List[PredictionRequest] = Field(..., max_items=100)

class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
    total_processing_time_ms: float

class HealthResponse(BaseModel):
    status: str
    uptime_seconds: float
    model_loaded: bool
    model_version: str

# Authentication
async def verify_api_key(x_api_key: str = Header(...)):
    """Verify API key."""
    valid_keys = ["demo-key-123", "prod-key-456"]  # In production, use env vars
    
    if x_api_key not in valid_keys:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return x_api_key

# Rate limiting (simplified - use Redis in production)
request_counts = {}

async def rate_limit(request: Request):
    """Simple rate limiting."""
    client_ip = request.client.host
    current_time = time.time()
    
    # Clean old entries
    request_counts[client_ip] = [
        t for t in request_counts.get(client_ip, [])
        if current_time - t < 60
    ]
    
    # Check limit (60 requests per minute)
    if len(request_counts.get(client_ip, [])) >= 60:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    # Add current request
    request_counts.setdefault(client_ip, []).append(current_time)

# Startup/Shutdown events
@app.on_event("startup")
async def startup_event():
    """Load model on startup."""
    global model
    try:
        model = joblib.load('/models/model.joblib')
        logger.info(f"Model v{model_version} loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down API")

# Exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "ValidationError",
            "message": str(exc),
            "request_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat()
        }
    )

# Endpoints
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {
        "message": "ML Model Inference API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy" if model is not None else "unhealthy",
        uptime_seconds=time.time() - app.state.start_time if hasattr(app.state, 'start_time') else 0,
        model_loaded=model is not None,
        model_version=model_version
    )

@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
async def predict(
    request: PredictionRequest,
    api_key: str = Depends(verify_api_key),
    _: None = Depends(rate_limit)
):
    """Make a single prediction."""
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    start_time = time.time()
    request_id = request.metadata.request_id if request.metadata else str(uuid.uuid4())
    
    try:
        # Prepare input
        features = np.array(request.features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].max()
        
        processing_time = (time.time() - start_time) * 1000
        
        logger.info(f"Prediction completed: request_id={request_id}, time={processing_time:.2f}ms")
        
        return PredictionResponse(
            prediction=float(prediction),
            probability=float(probability),
            model_version=model_version,
            request_id=request_id,
            processing_time_ms=processing_time
        )
    
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_predict", response_model=BatchPredictionResponse, tags=["Predictions"])
async def batch_predict(
    batch_request: BatchPredictionRequest,
    api_key: str = Depends(verify_api_key),
    _: None = Depends(rate_limit)
):
    """Make batch predictions."""
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    start_time = time.time()
    
    try:
        # Prepare batch input
        features = np.array([req.features for req in batch_request.requests])
        
        # Make predictions
        predictions = model.predict(features)
        probabilities = model.predict_proba(features).max(axis=1)
        
        # Create responses
        responses = []
        for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
            request_id = (
                batch_request.requests[i].metadata.request_id
                if batch_request.requests[i].metadata
                else str(uuid.uuid4())
            )
            
            responses.append(PredictionResponse(
                prediction=float(pred),
                probability=float(prob),
                model_version=model_version,
                request_id=request_id,
                processing_time_ms=0  # Individual timing not tracked in batch
            ))
        
        total_time = (time.time() - start_time) * 1000
        
        logger.info(f"Batch prediction completed: count={len(responses)}, time={total_time:.2f}ms")
        
        return BatchPredictionResponse(
            predictions=responses,
            total_processing_time_ms=total_time
        )
    
    except Exception as e:
        logger.error(f"Batch prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics", tags=["Monitoring"])
async def metrics():
    """Prometheus metrics endpoint."""
    # In production, use prometheus_client
    return {
        "requests_total": 1000,
        "requests_success": 950,
        "requests_failed": 50,
        "avg_latency_ms": 45.2
    }

if __name__ == "__main__":
    import uvicorn
    app.state.start_time = time.time()
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Step 3: Authentication & Authorization
**Duration**: 4-5 hours

**JWT Authentication**:
```python
# api/auth.py

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

class TokenData:
    def __init__(self, user_id: str, scopes: list):
        self.user_id = user_id
        self.scopes = scopes

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token."""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """Verify JWT token."""
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        scopes: list = payload.get("scopes", [])
        
        if user_id is None:
            raise credentials_exception
        
        return TokenData(user_id=user_id, scopes=scopes)
    
    except JWTError:
        raise credentials_exception

def require_scope(required_scope: str):
    """Dependency to check if user has required scope."""
    
    async def scope_checker(token_data: TokenData = Depends(verify_token)):
        if required_scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required scope: {required_scope}"
            )
        return token_data
    
    return scope_checker
```

### Step 4: Rate Limiting & Throttling
**Duration**: 3-4 hours

**Redis-based Rate Limiting**:
```python
# api/rate_limiting.py

from fastapi import HTTPException, Request
import redis
import time
from typing import Optional

class RateLimiter:
    
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_client = redis.from_url(redis_url, decode_responses=True)
    
    async def check_rate_limit(
        self,
        request: Request,
        max_requests: int = 100,
        window_seconds: int = 60
    ):
        """Check if request is within rate limit."""
        
        # Get client identifier (IP or user ID)
        client_id = self._get_client_id(request)
        key = f"rate_limit:{client_id}"
        
        # Get current count
        current = self.redis_client.get(key)
        
        if current is None:
            # First request in window
            pipe = self.redis_client.pipeline()
            pipe.set(key, 1)
            pipe.expire(key, window_seconds)
            pipe.execute()
            return
        
        current = int(current)
        
        if current >= max_requests:
            # Rate limit exceeded
            ttl = self.redis_client.ttl(key)
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded. Try again in {ttl} seconds.",
                headers={"Retry-After": str(ttl)}
            )
        
        # Increment counter
        self.redis_client.incr(key)
    
    def _get_client_id(self, request: Request) -> str:
        """Get client identifier from request."""
        
        # Try to get user ID from token
        if hasattr(request.state, 'user_id'):
            return f"user:{request.state.user_id}"
        
        # Fall back to IP address
        return f"ip:{request.client.host}"

# Token bucket algorithm
class TokenBucket:
    
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
    
    def consume(self, tokens: int = 1) -> bool:
        """Try to consume tokens."""
        
        # Refill tokens
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(
            self.capacity,
            self.tokens + elapsed * self.refill_rate
        )
        self.last_refill = now
        
        # Check if enough tokens
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        
        return False
```

### Step 5: Client SDK Generation
**Duration**: 4-6 hours

**Python SDK**:
```python
# client-sdk/python/ml_api_client.py

import requests
from typing import List, Dict, Optional
from dataclasses import dataclass
import time

@dataclass
class PredictionResult:
    prediction: float
    probability: float
    model_version: str
    request_id: str
    processing_time_ms: float

class MLAPIClient:
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'X-API-Key': api_key,
            'Content-Type': 'application/json'
        })
    
    def predict(self, features: List[float], request_id: Optional[str] = None) -> PredictionResult:
        """Make a single prediction."""
        
        payload = {
            'features': features,
            'metadata': {
                'request_id': request_id
            } if request_id else None
        }
        
        response = self.session.post(
            f'{self.base_url}/predict',
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()
        data = response.json()
        
        return PredictionResult(**data)
    
    def batch_predict(self, features_list: List[List[float]]) -> List[PredictionResult]:
        """Make batch predictions."""
        
        payload = {
            'requests': [
                {'features': features}
                for features in features_list
            ]
        }
        
        response = self.session.post(
            f'{self.base_url}/batch_predict',
            json=payload,
            timeout=60
        )
        
        response.raise_for_status()
        data = response.json()
        
        return [PredictionResult(**pred) for pred in data['predictions']]
    
    def health_check(self) -> Dict:
        """Check API health."""
        
        response = self.session.get(
            f'{self.base_url}/health',
            timeout=10
        )
        
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    client = MLAPIClient(
        base_url="https://api.company.com/v1",
        api_key="your-api-key"
    )
    
    # Single prediction
    result = client.predict([1500.50, 2, 0.75])
    print(f"Prediction: {result.prediction}, Probability: {result.probability}")
    
    # Batch prediction
    results = client.batch_predict([
        [1500.50, 2, 0.75],
        [2000.00, 3, 0.85],
        [500.25, 1, 0.60]
    ])
    
    for i, result in enumerate(results):
        print(f"Prediction {i+1}: {result.prediction}")
```

**JavaScript/TypeScript SDK**:
```typescript
// client-sdk/typescript/src/client.ts

export interface PredictionRequest {
  features: number[];
  metadata?: {
    request_id?: string;
    timestamp?: string;
  };
}

export interface PredictionResponse {
  prediction: number;
  probability: number;
  model_version: string;
  request_id: string;
  processing_time_ms: number;
}

export interface HealthResponse {
  status: string;
  uptime_seconds: number;
  model_loaded: boolean;
  model_version: string;
}

export class MLAPIClient {
  private baseUrl: string;
  private apiKey: string;

  constructor(baseUrl: string, apiKey: string) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.apiKey = apiKey;
  }

  async predict(features: number[], requestId?: string): Promise<PredictionResponse> {
    const response = await fetch(`${this.baseUrl}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': this.apiKey,
      },
      body: JSON.stringify({
        features,
        metadata: requestId ? { request_id: requestId } : undefined,
      }),
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    return response.json();
  }

  async batchPredict(featuresList: number[][]): Promise<PredictionResponse[]> {
    const response = await fetch(`${this.baseUrl}/batch_predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': this.apiKey,
      },
      body: JSON.stringify({
        requests: featuresList.map(features => ({ features })),
      }),
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    const data = await response.json();
    return data.predictions;
  }

  async healthCheck(): Promise<HealthResponse> {
    const response = await fetch(`${this.baseUrl}/health`, {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    return response.json();
  }
}

// Example usage
const client = new MLAPIClient('https://api.company.com/v1', 'your-api-key');

client.predict([1500.50, 2, 0.75])
  .then(result => {
    console.log(`Prediction: ${result.prediction}, Probability: ${result.probability}`);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

## 3. API Documentation Generation

**Automated Documentation**:
```python
# api/documentation.py

from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    """Generate custom OpenAPI schema."""
    
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="ML Model Inference API",
        version="1.0.0",
        description="Production API for ML model predictions with authentication and rate limiting",
        routes=app.routes,
    )
    
    # Add custom info
    openapi_schema["info"]["x-logo"] = {
        "url": "https://company.com/logo.png"
    }
    
    # Add security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-Key"
        },
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema
```

## 4. Quality Gates

### Gate 1: API Design
- [ ] OpenAPI specification complete
- [ ] All endpoints documented
- [ ] Request/response schemas defined
- [ ] Authentication strategy defined
- [ ] Rate limits configured

### Gate 2: Implementation
- [ ] All endpoints implemented
- [ ] Input validation working
- [ ] Authentication functional
- [ ] Rate limiting active
- [ ] Error handling comprehensive

### Gate 3: Documentation & SDKs
- [ ] API documentation generated
- [ ] Interactive docs accessible
- [ ] Python SDK generated and tested
- [ ] TypeScript SDK generated and tested
- [ ] Example code provided

## 5. Deliverables

### Required Outputs
1. **OpenAPI Specification** (`api-spec.yaml`)
2. **FastAPI Application** (`main.py`)
3. **Authentication Module** (`auth.py`)
4. **Rate Limiting Module** (`rate_limiting.py`)
5. **API Documentation** (`api-documentation.html`)
6. **Python SDK** (`client-sdk/python/`)
7. **TypeScript SDK** (`client-sdk/typescript/`)

### Evidence Package Structure
```
evidence/protocol-21-api-integration/
├── api/
│   ├── main.py
│   ├── auth.py
│   ├── rate_limiting.py
│   └── documentation.py
├── specs/
│   ├── api-spec.yaml
│   └── postman-collection.json
├── client-sdk/
│   ├── python/
│   │   ├── ml_api_client.py
│   │   ├── setup.py
│   │   └── README.md
│   └── typescript/
│       ├── src/client.ts
│       ├── package.json
│       └── README.md
├── docs/
│   ├── api-documentation.html
│   ├── authentication-guide.md
│   └── integration-examples.md
└── reports/
    ├── api_test_results.json
    └── integration_report.md
```

## 6. Common Pitfalls & Solutions

### Pitfall 1: No Input Validation
**Solution**: Use Pydantic models for strict validation

### Pitfall 2: Weak Authentication
**Solution**: Implement JWT with proper expiration and refresh

### Pitfall 3: No Rate Limiting
**Solution**: Use Redis-based rate limiting with token bucket

### Pitfall 4: Poor Documentation
**Solution**: Auto-generate from OpenAPI spec with examples

## 7. Success Criteria

- **API Availability**: >99.9% uptime
- **Response Time**: P95 <200ms, P99 <500ms
- **Authentication**: 100% of endpoints protected
- **Rate Limiting**: Effective throttling without false positives
- **Documentation**: Complete with working examples
- **SDK Coverage**: Python and TypeScript SDKs functional
