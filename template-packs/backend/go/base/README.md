# {{PROJECT_NAME}} Go Backend

A {{INDUSTRY}} {{PROJECT_TYPE}} backend built with Go, Echo framework, and GORM.

## Features

- 🚀 **Echo Framework** - High performance, minimalist Go web framework
- 🔐 **JWT Authentication** - Secure authentication with access/refresh tokens
- 👥 **User Management** - Complete user CRUD with role-based access control
- 🗄️ **GORM ORM** - Powerful ORM library for Go
- 🔄 **Database Migrations** - Automatic schema migrations
- 🚦 **Rate Limiting** - Built-in rate limiting middleware
- 🧪 **Testing** - Unit tests with testify
- 🐳 **Docker** - Multi-stage Docker build
- 📊 **Health Checks** - Service health monitoring
- 🔍 **Structured Logging** - Request logging with correlation IDs

## Prerequisites

- Go 1.21+
- PostgreSQL 12+
- Redis 6+ (optional, for caching)
- Docker (optional)
- Air (for hot reload in development)

## Quick Start

### 1. Clone and Setup

```bash
# Copy environment variables
cp .env.example .env

# Edit .env with your configuration
# Then run setup
make setup
```

### 2. Install Dependencies

```bash
make deps
```

### 3. Run Database Migrations

```bash
# Make sure PostgreSQL is running
make migrate
```

### 4. Run Development Server

```bash
# Run with hot reload (requires Air)
make dev

# Or run normally
make run
```

The API will be available at:
- API: http://localhost:8000
- Health Check: http://localhost:8000/health

## Project Structure

```
.
├── cmd/                    # Command line tools
├── internal/              # Private application code
│   ├── api/              # API layer
│   │   ├── handlers/     # HTTP handlers
│   │   ├── middleware/   # HTTP middleware
│   │   ├── requests/     # Request DTOs
│   │   ├── responses/    # Response DTOs
│   │   ├── router.go     # Route definitions
│   │   └── validator.go  # Request validation
│   ├── config/           # Configuration
│   ├── database/         # Database connection
│   ├── models/           # Data models
│   ├── services/         # Business logic
│   └── utils/            # Utility functions
├── migrations/           # Database migrations
├── scripts/              # Utility scripts
├── main.go              # Application entry point
├── go.mod               # Go module file
├── go.sum               # Go dependencies
├── Makefile             # Make commands
├── Dockerfile           # Docker configuration
└── .env.example         # Environment example
```

## API Endpoints

### Public Endpoints

- `GET /` - API information
- `GET /health` - Health check

### Authentication (`/api/v1/auth`)

- `POST /register` - Register new user
- `POST /login` - Login user
- `POST /refresh` - Refresh access token
- `POST /logout` - Logout user (requires auth)
- `POST /change-password` - Change password (requires auth)

### Users (`/api/v1/users`)

All user endpoints require authentication:

- `GET /` - List all users (admin only)
- `POST /` - Create new user (admin only)
- `GET /me` - Get current user profile
- `PUT /me` - Update current user profile
- `GET /:id` - Get user by ID (admin only)
- `PUT /:id` - Update user (admin only)
- `DELETE /:id` - Delete user (admin only)

## Development

### Available Make Commands

```bash
make help              # Show all available commands
make deps              # Download dependencies
make build             # Build the application
make run               # Run the application
make test              # Run tests
make test-coverage     # Run tests with coverage
make lint              # Run linter
make fmt               # Format code
make clean             # Clean build artifacts
make migrate           # Run database migrations
make migrate-down      # Rollback migrations
make docker-build      # Build Docker image
make docker-run        # Run in Docker
make dev               # Run with hot reload
make seed              # Seed database
```

### Environment Variables

Key environment variables (see `.env.example` for full list):

```env
# Server
SERVER_PORT=8000
SERVER_ENVIRONMENT=development

# Database
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=myapp_db

# JWT
JWT_SECRET=your-secret-key
JWT_ACCESS_TOKEN_DURATION=15m
JWT_REFRESH_TOKEN_DURATION=168h

# Redis (optional)
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Testing

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run specific test
go test ./internal/api/handlers -v

# Run with race detection
go test -race ./...
```

### Code Quality

```bash
# Format code
make fmt

# Run linter (requires golangci-lint)
make lint

# Run go vet
go vet ./...
```

### Hot Reload Development

Install Air for hot reload:

```bash
go install github.com/cosmtrek/air@latest
```

Then run:

```bash
make dev
```

## Architecture

### Clean Architecture Principles

- **Handlers**: HTTP request/response handling
- **Services**: Business logic implementation
- **Models**: Data structures and database schema
- **Utils**: Shared utilities and helpers

### Middleware Stack

1. **Logger**: Request/response logging
2. **Recover**: Panic recovery
3. **CORS**: Cross-origin resource sharing
4. **RequestID**: Request correlation
5. **RateLimiter**: Request rate limiting
6. **Auth**: JWT authentication
7. **RoleCheck**: Role-based access control

### Error Handling

- Consistent error response format
- Validation error details
- HTTP status code mapping
- Error logging with context

## Production Deployment

### Using Binary

```bash
# Build for production
make build

# Run binary
./build/{{PROJECT_NAME}}
```

### Using Docker

```bash
# Build image
make docker-build

# Run container
docker run -d \
  --name {{PROJECT_NAME}}-api \
  -p 8000:8000 \
  --env-file .env \
  {{PROJECT_NAME}}-backend
```

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

### Production Checklist

- [ ] Set strong JWT_SECRET
- [ ] Configure PostgreSQL with connection pooling
- [ ] Enable Redis for caching
- [ ] Set up proper logging
- [ ] Configure monitoring (Prometheus/Grafana)
- [ ] Set up backup strategy
- [ ] Enable HTTPS with TLS
- [ ] Configure rate limiting
- [ ] Set up health check monitoring

## Performance Tips

- Use connection pooling for database
- Enable query caching with Redis
- Use pagination for list endpoints
- Implement proper indexing
- Use prepared statements
- Enable gzip compression
- Use CDN for static assets

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   ```
   failed to connect to database
   ```
   - Check PostgreSQL is running
   - Verify database credentials
   - Ensure database exists

2. **Port Already in Use**
   ```
   bind: address already in use
   ```
   - Change SERVER_PORT in .env
   - Kill process using the port

3. **Migration Errors**
   - Check database connection
   - Verify migration files
   - Try manual migration

4. **JWT Errors**
   - Ensure JWT_SECRET is set
   - Check token format
   - Verify token expiration

5. **Import Errors**
   - Run `go mod tidy`
   - Check module name in go.mod
   - Verify import paths

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Code Style

- Follow Go conventions
- Use `gofmt` for formatting
- Write meaningful comments
- Add tests for new features
- Keep functions small and focused

## License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.