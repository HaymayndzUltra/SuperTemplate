# {{PROJECT_NAME}} FastAPI Backend

A high-performance {{INDUSTRY}} {{PROJECT_TYPE}} backend built with FastAPI, featuring modern async/await patterns, automatic API documentation, and enterprise-grade security.

## 🚀 Features

### Core Functionality
- ⚡ **FastAPI Framework**: Modern, fast web framework with automatic validation and serialization
- 🔐 **JWT Authentication**: Secure token-based authentication with access/refresh token rotation
- 👥 **User Management**: Complete user registration, profiles, and role-based access control
- 📚 **Auto Documentation**: Interactive API docs with Swagger UI and ReDoc
- 🗄️ **PostgreSQL Database**: Robust relational database with SQLAlchemy ORM
- 🔄 **Alembic Migrations**: Database version control and schema management
- 🚦 **Redis Caching**: High-performance caching and session management
- 📨 **Celery Integration**: Asynchronous task processing and background jobs
- 🧪 **Comprehensive Testing**: Full test suite with pytest and coverage reporting
- 🐳 **Docker Support**: Complete containerization for development and deployment

### Security & Performance
- **Authentication**: JWT with refresh token rotation and secure password hashing
- **Authorization**: Role-based access control (RBAC) with granular permissions
- **Data Validation**: Automatic request/response validation with Pydantic models
- **Rate Limiting**: Built-in API rate limiting and throttling
- **CORS Support**: Configurable cross-origin resource sharing
- **Security Headers**: Comprehensive security headers and HTTPS enforcement
- **Input Sanitization**: Automatic input validation and sanitization
- **SQL Injection Protection**: ORM-based queries with parameterized statements

### Development & Operations
- **Async/Await**: Full async support for high-performance I/O operations
- **Type Hints**: Complete type annotations for better IDE support and reliability
- **Environment Management**: Separate configurations for dev/staging/production
- **Health Monitoring**: Built-in health checks and monitoring endpoints
- **Logging**: Structured logging with configurable levels and outputs
- **Error Handling**: Comprehensive error handling with detailed error responses
- **API Versioning**: Built-in API versioning support
- **OpenAPI Compliance**: Full OpenAPI 3.0 specification compliance

## 📋 Prerequisites

### Required Software
- **Python** 3.11+ (recommended: 3.12)
- **PostgreSQL** 12+ (recommended: 15+)
- **Redis** 6+ (recommended: 7+)
- **Git** 2.30+

### Optional Software
- **Docker** 20.10+ (for containerized development)
- **Docker Compose** 2.0+ (for multi-service setup)
- **Node.js** 18+ (for frontend development)

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url> {{PROJECT_NAME}}
cd {{PROJECT_NAME}}

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy environment configuration
cp .env.example .env
# Edit .env with your specific configuration
```

### 2. Database Setup

```bash
# Create PostgreSQL database
createdb {{PROJECT_NAME}}_db

# Run database migrations
alembic upgrade head

# Initialize database with superuser
python scripts/init_db.py
```

### 3. Start Development Services

```bash
# Terminal 1: Start Redis server
redis-server

# Terminal 2: Start Celery worker
celery -A app.worker worker --loglevel=info

# Terminal 3: Start Celery beat (for scheduled tasks)
celery -A app.worker beat --loglevel=info

# Terminal 4: Start FastAPI development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Access the Application

- **API Base**: http://localhost:8000/api/v1/
- **Interactive Docs**: http://localhost:8000/api/docs
- **ReDoc Documentation**: http://localhost:8000/api/redoc
- **OpenAPI Schema**: http://localhost:8000/api/openapi.json
- **Health Check**: http://localhost:8000/health

## 📁 Project Structure

```
app/                        # Main application package
├── api/                   # API layer
│   ├── __init__.py
│   ├── deps.py           # Common dependencies (auth, db, etc.)
│   └── v1/               # API version 1
│       ├── __init__.py
│       ├── endpoints/    # Route handlers
│       │   ├── __init__.py
│       │   ├── auth.py   # Authentication endpoints
│       │   ├── users.py  # User management endpoints
│       │   └── health.py # Health check endpoints
│       └── router.py      # Main API router
├── core/                 # Core functionality
│   ├── __init__.py
│   ├── config.py         # Application configuration
│   ├── security.py       # Security utilities (JWT, password hashing)
│   └── exceptions.py     # Custom exceptions
├── crud/                 # Database operations
│   ├── __init__.py
│   ├── base.py          # Base CRUD class
│   └── crud_user.py     # User-specific CRUD operations
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   └── user.py          # User model
├── schemas/              # Pydantic schemas
│   ├── __init__.py
│   ├── token.py         # Authentication schemas
│   ├── user.py          # User schemas
│   └── msg.py           # Message schemas
├── services/             # Business logic layer
│   ├── __init__.py
│   └── user_service.py  # User business logic
├── utils/                # Utility functions
│   ├── __init__.py
│   └── email.py         # Email utilities
├── database.py           # Database connection and session
├── main.py              # FastAPI application entry point
└── worker.py            # Celery worker configuration

alembic/                  # Database migrations
├── versions/            # Migration files
├── env.py              # Alembic configuration
├── script.py.mako      # Migration template
└── alembic.ini         # Alembic settings

scripts/                 # Utility scripts
├── init_db.py         # Database initialization
└── setup.sh           # Project setup script

tests/                  # Test suite
├── __init__.py
├── conftest.py        # Test configuration and fixtures
├── test_main.py       # Main application tests
├── test_auth.py       # Authentication tests
├── test_users.py      # User management tests
└── test_performance.py # Performance tests
```

## 🔌 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Authentication | Request Body |
|--------|----------|-------------|----------------|--------------|
| POST | `/api/v1/auth/login/access-token` | Login with email/password | None | `email`, `password` |
| POST | `/api/v1/auth/login/test-token` | Test access token validity | Access token | None |
| POST | `/api/v1/auth/register` | Register new user | None | `email`, `password`, `full_name` |
| POST | `/api/v1/auth/password-recovery/{email}` | Request password reset | None | None |
| POST | `/api/v1/auth/reset-password` | Reset password with token | None | `token`, `new_password` |
| POST | `/api/v1/auth/refresh-token` | Refresh access token | Refresh token | None |
| POST | `/api/v1/auth/logout` | Logout user | Access token | None |

### User Management Endpoints

| Method | Endpoint | Description | Authentication | Request Body |
|--------|----------|-------------|----------------|--------------|
| GET | `/api/v1/users/` | List all users (paginated) | Admin | Query params: `skip`, `limit` |
| POST | `/api/v1/users/` | Create new user | Admin | `email`, `password`, `full_name`, `is_active` |
| GET | `/api/v1/users/me` | Get current user profile | Required | None |
| PUT | `/api/v1/users/me` | Update current user | Required | `full_name`, `email` |
| PATCH | `/api/v1/users/me` | Partial update current user | Required | Any user fields |
| GET | `/api/v1/users/{user_id}` | Get user by ID | Required | None |
| PUT | `/api/v1/users/{user_id}` | Update user (admin only) | Admin | `email`, `full_name`, `is_active` |
| DELETE | `/api/v1/users/{user_id}` | Delete user (admin only) | Admin | None |
| POST | `/api/v1/users/{user_id}/activate` | Activate user (admin only) | Admin | None |
| POST | `/api/v1/users/{user_id}/deactivate` | Deactivate user (admin only) | Admin | None |

### Health & Monitoring Endpoints

| Method | Endpoint | Description | Authentication | Response |
|--------|----------|-------------|----------------|----------|
| GET | `/health` | Basic health check | None | `{"status": "healthy"}` |
| GET | `/health/detailed` | Detailed health status | None | Database, Redis, external services |
| GET | `/health/ready` | Readiness probe | None | Service readiness status |
| GET | `/health/live` | Liveness probe | None | Service liveness status |

## 🛠️ Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app tests/
pytest --cov=app --cov-report=html tests/

# Run specific test file
pytest tests/test_main.py
pytest tests/test_auth.py
pytest tests/test_users.py

# Run tests with verbose output
pytest -v

# Run tests in parallel
pytest -n auto

# Run specific test method
pytest tests/test_auth.py::test_login_success

# Run tests with specific markers
pytest -m "not slow"
pytest -m "integration"
```

### Code Quality Tools

```bash
# Code formatting
black .                    # Format Python code
isort .                    # Sort imports
pre-commit run --all-files # Run all pre-commit hooks

# Linting
flake8 .                   # Python linting
pylint app/                # Advanced linting
bandit -r app/             # Security linting

# Type checking
mypy app/                  # Static type checking
mypy --strict app/         # Strict type checking

# Security checks
safety check               # Check for known vulnerabilities
pip-audit                  # Audit dependencies
```

### Database Operations

```bash
# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Downgrade one revision
alembic downgrade -1

# Downgrade to specific revision
alembic downgrade <revision_id>

# Show migration history
alembic history

# Show current revision
alembic current

# Show pending migrations
alembic heads

# Create empty migration
alembic revision -m "Empty migration"

# Generate SQL for migration (without applying)
alembic upgrade head --sql

# Stamp database with current revision
alembic stamp head
```

### Using Docker

```bash
# Build Docker image
docker build -t {{PROJECT_NAME}}-backend .

# Run container
docker run -d \
  --name {{PROJECT_NAME}}-api \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@db/dbname \
  -e REDIS_URL=redis://redis:6379/0 \
  {{PROJECT_NAME}}-backend

# Using docker-compose
docker-compose up -d

# View logs
docker-compose logs -f api
docker-compose logs -f redis
docker-compose logs -f postgres

# Execute commands in container
docker-compose exec api alembic upgrade head
docker-compose exec api python scripts/init_db.py

# Run tests in container
docker-compose exec api pytest

# Access database
docker-compose exec postgres psql -U postgres -d {{PROJECT_NAME}}_db

# Backup database
docker-compose exec postgres pg_dump -U postgres {{PROJECT_NAME}}_db > backup.sql

# Restore database
docker-compose exec -T postgres psql -U postgres {{PROJECT_NAME}}_db < backup.sql
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Application Configuration
PROJECT_NAME={{PROJECT_NAME}}
DEBUG=True
ENVIRONMENT=development

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/{{PROJECT_NAME}}_db
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Security Configuration
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
ALGORITHM=HS256

# First Superuser
FIRST_SUPERUSER=admin@example.com
FIRST_SUPERUSER_PASSWORD=changethis

# Email Configuration
SMTP_TLS=True
SMTP_PORT=587
SMTP_HOST=smtp.gmail.com
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAILS_FROM_EMAIL=noreply@yourdomain.com
EMAILS_FROM_NAME={{PROJECT_NAME}}

# CORS Configuration
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://127.0.0.1:3000"]

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# Logging Configuration
LOG_LEVEL=INFO
LOG_FORMAT=json

# Monitoring Configuration
SENTRY_DSN=your-sentry-dsn
```

### Production Configuration

For production deployment, ensure these settings:

```bash
# Security
DEBUG=False
SECRET_KEY=your-production-secret-key
ENVIRONMENT=production

# Database
DATABASE_URL=postgresql://user:password@prod-db:5432/{{PROJECT_NAME}}_prod
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=30

# Redis
REDIS_URL=redis://prod-redis:6379/0

# Email
SMTP_HOST=smtp.your-provider.com
SMTP_USER=noreply@yourdomain.com
SMTP_PASSWORD=your-email-password
EMAILS_FROM_EMAIL=noreply@yourdomain.com

# CORS
BACKEND_CORS_ORIGINS=["https://yourdomain.com", "https://www.yourdomain.com"]

# Monitoring
SENTRY_DSN=your-production-sentry-dsn
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Generate strong `SECRET_KEY`
- [ ] Configure production `DATABASE_URL`
- [ ] Set up Redis for production
- [ ] Configure email settings
- [ ] Set up monitoring (Sentry, DataDog)
- [ ] Enable HTTPS
- [ ] Set up backup strategy
- [ ] Configure log aggregation
- [ ] Set up health checks
- [ ] Configure rate limiting
- [ ] Set up API documentation
- [ ] Configure CORS properly
- [ ] Set up SSL certificates

### Using Gunicorn

```bash
# Install Gunicorn with Uvicorn workers
pip install gunicorn uvicorn[standard]

# Run with Gunicorn
gunicorn app.main:app \
  -w 4 \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --timeout 60 \
  --keep-alive 2 \
  --max-requests 1000 \
  --max-requests-jitter 100 \
  --preload \
  --log-level info \
  --access-logfile - \
  --error-logfile -
```

### Using Docker Production

```bash
# Build production image
docker build -f Dockerfile.prod -t {{PROJECT_NAME}}-backend:latest .

# Run production container
docker run -d \
  --name {{PROJECT_NAME}}-api \
  -p 8000:8000 \
  -e DEBUG=False \
  -e SECRET_KEY=your-production-secret \
  -e DATABASE_URL=postgresql://user:pass@db:5432/prod_db \
  -e REDIS_URL=redis://redis:6379/0 \
  {{PROJECT_NAME}}-backend:latest
```

### Using Docker Compose Production

```yaml
version: '3.8'
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.prod
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
    depends_on:
      - postgres
      - redis
    restart: unless-stopped

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    restart: unless-stopped

volumes:
  postgres_data:
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Database Connection Error
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Verify connection
psql -h localhost -U postgres -d {{PROJECT_NAME}}_db

# Check environment variables
echo $DATABASE_URL

# Test connection from Python
python -c "
from sqlalchemy import create_engine
engine = create_engine('$DATABASE_URL')
print(engine.connect())
"
```

#### 2. Redis Connection Error
```bash
# Check Redis status
sudo systemctl status redis

# Test Redis connection
redis-cli ping

# Check Redis configuration
redis-cli config get "*"

# Test from Python
python -c "
import redis
r = redis.from_url('$REDIS_URL')
print(r.ping())
"
```

#### 3. Import Errors
```bash
# Check Python path
python -c "import sys; print(sys.path)"

# Verify virtual environment
which python
pip list

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### 4. Migration Errors
```bash
# Check migration status
alembic current
alembic heads

# Sync migration state
alembic stamp head

# Create new migration
alembic revision --autogenerate -m "Fix migration"

# Apply migrations
alembic upgrade head
```

#### 5. CORS Errors
```bash
# Check CORS settings
python -c "
from app.core.config import settings
print(settings.BACKEND_CORS_ORIGINS)
"

# Add frontend URL to CORS settings
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://127.0.0.1:3000"]
```

#### 6. JWT Token Issues
```bash
# Check JWT settings
python -c "
from app.core.config import settings
print(f'Access token expire: {settings.ACCESS_TOKEN_EXPIRE_MINUTES}')
print(f'Algorithm: {settings.ALGORITHM}')
"

# Test token generation
python -c "
from app.core.security import create_access_token
token = create_access_token(subject='test@example.com')
print(token)
"
```

### Performance Optimization

#### Database Optimization
```bash
# Analyze slow queries
python -c "
from app.database import engine
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM pg_stat_activity'))
    print(result.fetchall())
"

# Add database indexes
alembic revision -m "Add indexes"
# Add indexes in migration file

# Use async database operations
from sqlalchemy.ext.asyncio import AsyncSession
async with AsyncSession(engine) as session:
    result = await session.execute(query)
```

#### Caching Optimization
```bash
# Test Redis caching
python -c "
import redis
r = redis.from_url('$REDIS_URL')
r.set('test', 'value', ex=300)
print(r.get('test'))
"

# Use cache decorators
from functools import lru_cache
@lru_cache(maxsize=128)
def expensive_function(param):
    return result
```

## 📊 Monitoring & Logging

### Health Checks
- **Basic Health**: `/health` - Returns 200 if service is running
- **Detailed Health**: `/health/detailed` - Checks database, Redis, external services
- **Readiness**: `/health/ready` - Kubernetes readiness probe
- **Liveness**: `/health/live` - Kubernetes liveness probe

### Logging Configuration
```python
import logging
import sys
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format=settings.LOG_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log")
    ]
)

# Structured logging
import structlog
logger = structlog.get_logger()
logger.info("User logged in", user_id=user.id, email=user.email)
```

### Metrics and Monitoring
```python
# Prometheus metrics
from prometheus_client import Counter, Histogram, generate_latest

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')

# Custom metrics endpoint
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

## 🔒 Security

### Security Features
- **Authentication**: JWT with refresh token rotation
- **Authorization**: Role-based access control (RBAC)
- **Data Validation**: Automatic request/response validation
- **Rate Limiting**: API rate limiting per user/IP
- **CORS Protection**: Configurable cross-origin policies
- **Input Sanitization**: Automatic input validation
- **SQL Injection Protection**: ORM-based queries only
- **Password Security**: bcrypt hashing with salt

### Security Checklist
- [ ] Use HTTPS in production
- [ ] Set secure cookie flags
- [ ] Implement proper CORS policies
- [ ] Use environment variables for secrets
- [ ] Regular security updates
- [ ] Implement rate limiting
- [ ] Monitor for suspicious activity
- [ ] Regular security audits
- [ ] Use strong password policies
- [ ] Implement account lockout

## 📚 API Documentation

FastAPI automatically generates comprehensive API documentation:

### Interactive Documentation
1. **Swagger UI**: http://localhost:8000/api/docs
   - Interactive interface to test API endpoints
   - Shows request/response schemas
   - Allows testing with authentication
   - Supports file uploads and complex data types

2. **ReDoc**: http://localhost:8000/api/redoc
   - Alternative documentation interface
   - Better for reading and sharing
   - Clean, professional appearance
   - Mobile-friendly design

3. **OpenAPI Schema**: http://localhost:8000/api/openapi.json
   - Machine-readable API specification
   - Can be used for client generation
   - Supports code generation tools
   - Integrates with API testing tools

### Custom Documentation
```python
from fastapi import FastAPI

app = FastAPI(
    title="{{PROJECT_NAME}} API",
    description="A comprehensive API for {{PROJECT_NAME}}",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Add custom documentation
@app.get("/api/docs/custom", include_in_schema=False)
async def custom_docs():
    return {"message": "Custom documentation endpoint"}
```

## 📄 License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive tests
- Update documentation
- Use type hints
- Follow async/await patterns
- Add proper error handling

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the API documentation
- Review the troubleshooting section
- Contact the development team

---

**{{PROJECT_NAME}}** - Built with FastAPI for high-performance web applications.