# {{PROJECT_NAME}} NestJS Backend

A {{INDUSTRY}} {{PROJECT_TYPE}} backend built with NestJS, TypeScript, and TypeORM.

## Features

- 🚀 **NestJS** - Progressive Node.js framework for building efficient and scalable server-side applications
- 🔐 **JWT Authentication** - Secure authentication with access/refresh tokens
- 👥 **User Management** - Complete user CRUD with role-based access control
- 📚 **Auto Documentation** - Swagger/OpenAPI documentation
- 🗄️ **TypeORM** - Powerful ORM for TypeScript and JavaScript
- 🔄 **Database Migrations** - Version control for your database
- 🚦 **Rate Limiting** - Protect your API from abuse
- 🧪 **Testing** - Unit and E2E test suites
- 🐳 **Docker** - Production-ready Docker configuration
- 📊 **Health Checks** - Comprehensive health monitoring
- 🔍 **Logging** - Structured logging with request tracking

## Prerequisites

- Node.js 18+
- PostgreSQL 12+
- Redis 6+ (for rate limiting)
- Docker (optional)

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Environment Setup

```bash
# Copy environment variables
cp .env.example .env

# Edit .env with your configuration
```

### 3. Database Setup

```bash
# Run migrations
npm run migration:run

# Or generate new migration from entities
npm run migration:generate -- -n MigrationName
```

### 4. Run Development Server

```bash
# Development
npm run start:dev

# Production
npm run build
npm run start:prod

# Debug mode
npm run start:debug
```

The API will be available at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/api/docs
- Health Check: http://localhost:8000/health

## Project Structure

```
src/
├── auth/                 # Authentication module
│   ├── strategies/      # Passport strategies
│   ├── guards/          # Auth guards
│   ├── dto/             # Auth DTOs
│   └── entities/        # Auth entities
├── users/               # Users module
│   ├── dto/             # User DTOs
│   ├── entities/        # User entities
│   └── users.service.ts # User business logic
├── common/              # Shared module
│   ├── decorators/      # Custom decorators
│   ├── guards/          # Global guards
│   ├── interceptors/    # Global interceptors
│   ├── filters/         # Exception filters
│   └── enums/           # Shared enums
├── config/              # Configuration
│   ├── configuration.ts # App configuration
│   ├── typeorm.config.ts # Database config
│   └── throttler.config.ts # Rate limit config
├── health/              # Health check module
├── app.module.ts        # Root module
└── main.ts             # Application entry point

test/                    # Test files
├── e2e/                # End-to-end tests
└── unit/               # Unit tests
```

## API Documentation

### Authentication Endpoints

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - Logout user
- `POST /api/v1/auth/change-password` - Change password

### User Endpoints

- `GET /api/v1/users` - Get all users (Admin)
- `POST /api/v1/users` - Create user (Admin)
- `GET /api/v1/users/me` - Get current user
- `PATCH /api/v1/users/me` - Update current user
- `GET /api/v1/users/:id` - Get user by ID (Admin)
- `PATCH /api/v1/users/:id` - Update user (Admin)
- `DELETE /api/v1/users/:id` - Delete user (Admin)

### Health Check

- `GET /api/v1/health` - Comprehensive health check
- `GET /api/v1/health/simple` - Simple health check

## Development

### Environment Variables

Key environment variables (see `.env.example` for full list):

```env
# Application
NODE_ENV=development
PORT=8000

# Database
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_DATABASE=myapp_db

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRATION=3600

# Rate Limiting
THROTTLE_TTL=60
THROTTLE_LIMIT=10
```

### Database Migrations

```bash
# Generate migration from entity changes
npm run migration:generate -- -n MigrationName

# Create empty migration
npm run typeorm migration:create -- -n MigrationName

# Run pending migrations
npm run migration:run

# Revert last migration
npm run migration:revert

# Show migrations
npm run typeorm migration:show
```

### Testing

```bash
# Unit tests
npm run test

# E2E tests
npm run test:e2e

# Test coverage
npm run test:cov

# Watch mode
npm run test:watch

# Debug tests
npm run test:debug
```

### Code Quality

```bash
# Format code
npm run format

# Lint code
npm run lint

# Type checking
npm run build
```

### Docker

```bash
# Build image
docker build -t {{PROJECT_NAME}}-backend .

# Run container
docker run -d \
  --name {{PROJECT_NAME}}-api \
  -p 8000:8000 \
  -e DB_HOST=host.docker.internal \
  -e DB_PASSWORD=yourpassword \
  {{PROJECT_NAME}}-backend

# Using docker-compose
docker-compose up -d
```

## Architecture Decisions

### Modular Structure
- Feature-based module organization
- Clear separation of concerns
- Dependency injection for testability

### Security
- JWT with refresh tokens
- Role-based access control (RBAC)
- Request rate limiting
- Input validation and sanitization
- CORS configuration
- Helmet for security headers

### Database
- TypeORM for database abstraction
- Migration-based schema management
- Entity relationships with decorators
- Query builder for complex queries

### Error Handling
- Global exception filters
- Standardized error responses
- Proper HTTP status codes
- Detailed error logging

## Production Deployment

### Prerequisites
- Node.js 18+ on server
- PostgreSQL database
- Redis instance
- PM2 or similar process manager

### Deployment Steps

1. **Build Application**
   ```bash
   npm run build
   ```

2. **Set Environment Variables**
   ```bash
   export NODE_ENV=production
   export DATABASE_URL=postgresql://...
   # Set other production variables
   ```

3. **Run Migrations**
   ```bash
   npm run migration:run
   ```

4. **Start Application**
   ```bash
   # With PM2
   pm2 start dist/main.js --name {{PROJECT_NAME}}-api

   # Or directly
   node dist/main.js
   ```

### Performance Tips
- Enable clustering with PM2
- Use Redis for caching
- Implement database connection pooling
- Enable gzip compression
- Use CDN for static assets

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check PostgreSQL is running
   - Verify database credentials
   - Ensure database exists

2. **Migration Errors**
   - Check database connection
   - Verify migration files
   - Try reverting and re-running

3. **JWT Errors**
   - Ensure JWT_SECRET is set
   - Check token expiration
   - Verify token format

4. **CORS Issues**
   - Add frontend URL to CORS_ORIGINS
   - Check request headers

5. **Rate Limiting**
   - Adjust THROTTLE_LIMIT
   - Check Redis connection

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Write/update tests
5. Submit pull request

## License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.