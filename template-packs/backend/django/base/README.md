# {{PROJECT_NAME}} Django Backend

A production-ready {{INDUSTRY}} {{PROJECT_TYPE}} backend built with Django REST Framework, featuring comprehensive authentication, user management, and modern development practices.

## 🚀 Features

### Core Functionality
- **JWT Authentication**: Secure token-based authentication with refresh tokens
- **User Management**: Complete user registration, profiles, and account management
- **Activity Tracking**: Comprehensive audit logs and user activity monitoring
- **Health Monitoring**: Built-in health check endpoints for monitoring
- **API Documentation**: Auto-generated Swagger/ReDoc documentation
- **Async Processing**: Celery integration for background tasks
- **Caching**: Redis-based caching for improved performance
- **Database**: PostgreSQL with optimized queries and migrations

### Security & Compliance
- **Authentication**: JWT with refresh token rotation
- **Authorization**: Role-based access control (RBAC)
- **Data Protection**: Encrypted sensitive data storage
- **Audit Logging**: Comprehensive activity tracking
- **CORS Support**: Configurable cross-origin resource sharing
- **Rate Limiting**: Built-in API rate limiting
- **Input Validation**: Comprehensive request validation

### Development & Operations
- **Docker Support**: Complete containerization setup
- **Environment Management**: Separate settings for dev/staging/production
- **Testing**: Comprehensive test suite with coverage reporting
- **Code Quality**: Black formatting, Flake8 linting, MyPy type checking
- **Database Migrations**: Automated schema management
- **Monitoring**: Health checks and performance metrics

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

### 2. Database Configuration

```bash
# Create PostgreSQL database
createdb {{PROJECT_NAME}}_db

# Run database migrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser

# Load initial data (optional)
python manage.py loaddata fixtures/initial_data.json
```

### 3. Start Development Services

```bash
# Terminal 1: Start Redis server
redis-server

# Terminal 2: Start Celery worker
celery -A {{PROJECT_NAME}} worker --loglevel=info

# Terminal 3: Start Celery beat (for scheduled tasks)
celery -A {{PROJECT_NAME}} beat --loglevel=info

# Terminal 4: Start Django development server
python manage.py runserver
```

### 4. Access the Application

- **API Base**: http://localhost:8000/api/v1/
- **Admin Panel**: http://localhost:8000/admin/
- **API Documentation**: http://localhost:8000/api/docs/
- **ReDoc Documentation**: http://localhost:8000/api/redoc/
- **Health Check**: http://localhost:8000/health/

## 📁 Project Structure

```
{{PROJECT_NAME}}/
├── settings/                 # Django settings configuration
│   ├── __init__.py
│   ├── base.py              # Base settings (shared)
│   ├── development.py       # Development environment
│   ├── production.py        # Production environment
│   └── testing.py           # Testing environment
├── urls.py                  # Main URL configuration
├── wsgi.py                  # WSGI application entry point
├── asgi.py                  # ASGI application entry point
└── celery.py               # Celery configuration

apps/                        # Django applications
├── authentication/         # Authentication & authorization
│   ├── __init__.py
│   ├── models.py           # User, Token models
│   ├── views.py            # Login, logout, token refresh
│   ├── serializers.py      # API serializers
│   ├── urls.py             # Authentication URLs
│   ├── permissions.py      # Custom permissions
│   ├── middleware.py       # Custom middleware
│   └── tests.py            # Authentication tests
├── users/                  # User management
│   ├── __init__.py
│   ├── models.py           # Profile, Activity models
│   ├── views.py            # User CRUD operations
│   ├── serializers.py      # User serializers
│   ├── urls.py             # User URLs
│   ├── managers.py         # Custom model managers
│   └── tests.py            # User management tests
└── core/                   # Core functionality
    ├── __init__.py
    ├── models.py           # Base models, utilities
    ├── views.py            # Health checks, API info
    ├── serializers.py      # Core serializers
    ├── urls.py             # Core URLs
    ├── utils.py            # Utility functions
    ├── exceptions.py       # Custom exceptions
    └── tests.py            # Core functionality tests

scripts/                    # Utility scripts
├── setup.sh               # Initial project setup
├── migrate.sh             # Database migration helper
├── backup.sh              # Database backup script
└── deploy.sh              # Deployment script

tests/                      # Integration tests
├── __init__.py
├── test_api.py            # API integration tests
├── test_auth.py           # Authentication tests
└── test_performance.py    # Performance tests
```

## 🔌 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/api/v1/auth/register/` | User registration | None |
| POST | `/api/v1/auth/login/` | User login | None |
| POST | `/api/v1/auth/logout/` | User logout | Required |
| POST | `/api/v1/auth/token/refresh/` | Refresh JWT token | Refresh token |
| GET | `/api/v1/auth/profile/` | Get current user profile | Required |
| PATCH | `/api/v1/auth/profile/` | Update user profile | Required |
| POST | `/api/v1/auth/change-password/` | Change password | Required |
| POST | `/api/v1/auth/forgot-password/` | Request password reset | None |
| POST | `/api/v1/auth/reset-password/` | Reset password | Reset token |

### User Management Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/v1/users/` | List users (paginated) | Required |
| GET | `/api/v1/users/{id}/` | Get user details | Required |
| PATCH | `/api/v1/users/{id}/` | Update user | Required (self or admin) |
| DELETE | `/api/v1/users/{id}/` | Delete user | Required (admin) |
| POST | `/api/v1/users/{id}/activate/` | Activate user | Required (admin) |
| POST | `/api/v1/users/{id}/deactivate/` | Deactivate user | Required (admin) |
| GET | `/api/v1/users/{id}/activities/` | Get user activities | Required |
| GET | `/api/v1/users/search/` | Search users | Required |
| GET | `/api/v1/users/stats/` | User statistics | Required (admin) |

### Core Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/health/` | Health check | None |
| GET | `/api/v1/` | API information | None |
| GET | `/api/v1/stats/` | System statistics | Required (admin) |
| GET | `/api/v1/version/` | API version info | None |

## 🛠️ Development

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML coverage report

# Run specific app tests
python manage.py test apps.authentication
python manage.py test apps.users
python manage.py test apps.core

# Run tests in parallel
python manage.py test --parallel

# Run specific test methods
python manage.py test apps.authentication.tests.AuthTestCase.test_login
```

### Code Quality Tools

```bash
# Code formatting
black .                    # Format Python code
isort .                    # Sort imports
pre-commit run --all-files # Run all pre-commit hooks

# Linting
flake8 .                   # Python linting
pylint apps/               # Advanced linting
bandit -r apps/            # Security linting

# Type checking
mypy apps/                 # Static type checking
mypy --strict apps/        # Strict type checking

# Security checks
safety check               # Check for known vulnerabilities
pip-audit                  # Audit dependencies
```

### Database Operations

```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Create migration from model changes
python manage.py makemigrations apps.users

# Apply specific migration
python manage.py migrate apps.users 0001

# Rollback migration
python manage.py migrate apps.users 0000

# Create empty migration
python manage.py makemigrations --empty apps.users

# Generate SQL for migration
python manage.py sqlmigrate apps.users 0001
```

### Using Docker

```bash
# Build Docker image
docker build -t {{PROJECT_NAME}}-backend .

# Run with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f backend
docker-compose logs -f redis
docker-compose logs -f postgres

# Execute management commands
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic

# Run tests in container
docker-compose exec backend python manage.py test

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
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/{{PROJECT_NAME}}_db
DATABASE_NAME={{PROJECT_NAME}}_db
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# JWT Configuration
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_LIFETIME=3600
JWT_REFRESH_TOKEN_LIFETIME=604800

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
CORS_ALLOW_CREDENTIALS=True

# Static Files
STATIC_URL=/static/
STATIC_ROOT=/app/staticfiles/
MEDIA_URL=/media/
MEDIA_ROOT=/app/media/

# Logging
LOG_LEVEL=INFO
LOG_FILE=/app/logs/django.log

# Security
SECURE_SSL_REDIRECT=False
SECURE_HSTS_SECONDS=0
SECURE_HSTS_INCLUDE_SUBDOMAINS=False
SECURE_HSTS_PRELOAD=False
```

### Production Configuration

For production deployment, ensure these settings:

```bash
# Security
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

# Database
DATABASE_URL=postgresql://user:password@prod-db:5432/{{PROJECT_NAME}}_prod

# Redis
REDIS_URL=redis://prod-redis:6379/0

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=noreply@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password

# Monitoring
SENTRY_DSN=your-sentry-dsn
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Generate new `SECRET_KEY`
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Set up SSL/TLS certificates
- [ ] Configure production database
- [ ] Set up Redis for production
- [ ] Configure email backend
- [ ] Set up monitoring (Sentry, DataDog)
- [ ] Configure static/media file serving
- [ ] Set up backup strategy
- [ ] Configure logging
- [ ] Set up health checks
- [ ] Configure rate limiting
- [ ] Set up API documentation

### Using Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn {{PROJECT_NAME}}.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 2 \
    --timeout 60 \
    --keep-alive 2 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --preload \
    --log-level info \
    --access-logfile - \
    --error-logfile -
```

### Using uWSGI

```bash
# Install uWSGI
pip install uwsgi

# Run with uWSGI
uwsgi --http :8000 \
    --module {{PROJECT_NAME}}.wsgi \
    --processes 4 \
    --threads 2 \
    --master \
    --enable-threads \
    --single-interpreter \
    --harakiri 60 \
    --max-requests 1000 \
    --vacuum \
    --die-on-term
```

### Docker Production Deployment

```bash
# Build production image
docker build -f Dockerfile.prod -t {{PROJECT_NAME}}-backend:latest .

# Run production container
docker run -d \
    --name {{PROJECT_NAME}}-backend \
    -p 8000:8000 \
    -e DEBUG=False \
    -e SECRET_KEY=your-production-secret \
    -e DATABASE_URL=postgresql://user:pass@db:5432/prod_db \
    {{PROJECT_NAME}}-backend:latest
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
```

#### 2. Redis Connection Error
```bash
# Check Redis status
sudo systemctl status redis

# Test Redis connection
redis-cli ping

# Check Redis configuration
redis-cli config get "*"
```

#### 3. Migration Errors
```bash
# Reset migrations (development only)
python manage.py migrate --fake-initial

# Check migration status
python manage.py showmigrations

# Create new migration
python manage.py makemigrations --empty apps.users
```

#### 4. Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check static file settings
python manage.py diffsettings | grep STATIC

# Verify file permissions
ls -la staticfiles/
```

#### 5. CORS Errors
```bash
# Check CORS settings
python manage.py shell
>>> from django.conf import settings
>>> print(settings.CORS_ALLOWED_ORIGINS)

# Add frontend URL to CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

#### 6. JWT Token Issues
```bash
# Check JWT settings
python manage.py shell
>>> from django.conf import settings
>>> print(settings.SIMPLE_JWT)

# Verify token generation
python manage.py shell
>>> from rest_framework_simplejwt.tokens import RefreshToken
>>> token = RefreshToken.for_user(user)
>>> print(token.access_token)
```

### Performance Optimization

#### Database Optimization
```bash
# Analyze slow queries
python manage.py shell
>>> from django.db import connection
>>> connection.queries

# Add database indexes
python manage.py makemigrations --empty apps.users
# Add indexes in migration file

# Use select_related and prefetch_related
User.objects.select_related('profile').prefetch_related('activities')
```

#### Caching Optimization
```bash
# Test Redis caching
python manage.py shell
>>> from django.core.cache import cache
>>> cache.set('test', 'value', 300)
>>> cache.get('test')

# Use cache decorators
from django.views.decorators.cache import cache_page
@cache_page(60 * 15)  # Cache for 15 minutes
```

## 📊 Monitoring & Logging

### Health Checks
- **Basic Health**: `/health/` - Returns 200 if service is running
- **Database Health**: `/health/db/` - Checks database connectivity
- **Redis Health**: `/health/redis/` - Checks Redis connectivity
- **Detailed Health**: `/health/detailed/` - Comprehensive health status

### Logging Configuration
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/app/logs/django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}
```

## 🔒 Security

### Security Features
- **Authentication**: JWT with refresh token rotation
- **Authorization**: Role-based access control
- **Data Protection**: Field-level encryption for sensitive data
- **Audit Logging**: Comprehensive activity tracking
- **Rate Limiting**: API rate limiting per user/IP
- **CORS Protection**: Configurable cross-origin policies
- **Input Validation**: Comprehensive request validation
- **SQL Injection Protection**: ORM-based queries only

### Security Checklist
- [ ] Use HTTPS in production
- [ ] Set secure cookie flags
- [ ] Implement proper CORS policies
- [ ] Use environment variables for secrets
- [ ] Regular security updates
- [ ] Implement rate limiting
- [ ] Monitor for suspicious activity
- [ ] Regular security audits

## 📄 License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Review the troubleshooting section
- Contact the development team

---

**{{PROJECT_NAME}}** - Built with Django REST Framework for modern web applications.