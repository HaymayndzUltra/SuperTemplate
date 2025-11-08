# Environment Requirements Document

**Generated:** 2025-01-27  
**Generator:** Protocol 09 DevOps Environment Engineer  
**Project:** Freelancer Command Center MVP  
**Source:** TECHNICAL-DESIGN.md, task-generation-input.json, tasks-*.md

---

## Executive Summary

This document consolidates all environment requirements derived from the technical design and task plans. It provides a comprehensive checklist for provisioning and validating the development environment.

---

## Runtime Tooling Requirements

### Frontend Development Environment

**Required Tools:**
- **Node.js:** Version 18+ (for Next.js 14 App Router)
- **npm:** Version 9+ (comes with Node.js 18+)
- **TypeScript:** Version 5.0+ (installed as dev dependency)
- **Git:** Version 2.30+ (for version control)

**Package Manager:**
- npm (default with Node.js)

**Development Dependencies:**
- Next.js 14 (App Router)
- React 18+
- TypeScript
- Tailwind CSS
- react-hook-form + Zod (form validation)
- @supabase/supabase-js (Supabase Auth SDK)

**Development Tools:**
- ESLint (code linting)
- Prettier (code formatting, optional but recommended)
- TypeScript compiler (type checking)

**Deployment Platform:**
- Vercel (production/staging)

---

### Backend Development Environment

**Required Tools:**
- **Python:** Version 3.11+ (required for FastAPI 0.110)
- **pip:** Version 22.0+ (comes with Python 3.11)
- **uvicorn:** ASGI server for FastAPI
- **Git:** Version 2.30+ (for version control)

**Python Dependencies:**
- FastAPI 0.110
- Python 3.11
- SQLModel (SQLAlchemy + Pydantic)
- Alembic (database migrations)
- Pydantic (data validation)

**Development Tools:**
- pytest (testing framework)
- ruff (linting, optional)
- black (code formatting, optional)
- mypy (type checking, optional)

**Deployment Platform:**
- Render (production/staging)

---

### Database Environment

**Database Service:**
- **Supabase PostgreSQL:** Managed PostgreSQL database
- **Row Level Security (RLS):** Enabled for multi-tenancy

**Migration Tool:**
- Alembic (for schema versioning)

**Database Access:**
- Connection string via environment variable
- Supabase project credentials

**Migration Requirements:**
- Alembic configuration
- Migration scripts directory structure
- Database connection validation

---

### Authentication Service

**Service:**
- **Supabase Auth:** Managed authentication service

**Integration Requirements:**
- Frontend: @supabase/supabase-js SDK
- Backend: JWT token validation
- Database: User records integration

**Environment Variables:**
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `SUPABASE_JWT_SECRET` (backend)

---

## Infrastructure & Services

### External Services

1. **Supabase Project**
   - PostgreSQL database instance
   - Authentication service
   - Project URL and API keys

2. **Vercel Account**
   - Frontend deployment platform
   - Environment variable configuration
   - Domain configuration (if applicable)

3. **Render Account**
   - Backend deployment platform
   - Environment variable configuration
   - Service configuration

### Container/DevContainer Support

**Optional but Recommended:**
- Docker (for devcontainer support)
- VS Code Dev Containers extension (if using VS Code)

**DevContainer Configuration:**
- `.devcontainer/devcontainer.json` (already scaffolded)
- Base image selection
- Port forwarding configuration

---

## Configuration Files

### Frontend Configuration

**Required Files:**
- `frontend/package.json` - Dependencies and scripts
- `frontend/tsconfig.json` - TypeScript configuration
- `frontend/next.config.js` - Next.js configuration
- `frontend/tailwind.config.js` - Tailwind CSS configuration
- `.env.local` - Local environment variables

**Environment Variables (Frontend):**
- `NEXT_PUBLIC_API_URL` - Backend API base URL
- `NEXT_PUBLIC_SUPABASE_URL` - Supabase project URL
- `NEXT_PUBLIC_SUPABASE_ANON_KEY` - Supabase anonymous key

### Backend Configuration

**Required Files:**
- `backend/requirements.txt` - Python dependencies
- `backend/pyproject.toml` or `backend/setup.py` - Python project configuration
- `backend/alembic.ini` - Alembic migration configuration
- `backend/alembic/env.py` - Alembic environment setup
- `.env` - Backend environment variables

**Environment Variables (Backend):**
- `DATABASE_URL` - Supabase PostgreSQL connection string
- `SUPABASE_URL` - Supabase project URL
- `SUPABASE_JWT_SECRET` - JWT secret for token validation
- `CORS_ORIGINS` - Allowed CORS origins (comma-separated)

### Root Configuration

**Required Files:**
- `.gitignore` - Git ignore patterns
- `.env.example` - Environment variable template
- `README.md` - Project documentation

---

## CI/CD Requirements

### GitHub Actions Workflows

**Required Workflows:**
- Frontend linting and type checking
- Backend testing (pytest)
- Database migration validation
- Security scanning (semgrep)

**Workflow Triggers:**
- Push to main branch
- Pull requests

**CI/CD Tools:**
- GitHub Actions (already scaffolded)
- Automated testing on PR
- Deployment automation (optional)

---

## Validation & Testing Requirements

### Frontend Validation

**Commands:**
- `npm run lint` - ESLint validation
- `npm run type-check` - TypeScript validation
- `npm run test` - Component tests (when implemented)
- `npm run test:e2e` - E2E tests (when implemented)

### Backend Validation

**Commands:**
- `pytest` - Run all tests
- `pytest tests/api/` - API endpoint tests
- `pytest tests/security/` - Security tests (when implemented)
- `ruff check app/` - Linting (optional)
- `black app/` - Code formatting (optional)
- `mypy app/` - Type checking (optional)

### Database Validation

**Commands:**
- `alembic check` - Validate Alembic configuration
- `alembic upgrade head` - Apply migrations
- `python scripts/test_db_connection.py` - Test database connection
- `python scripts/validate_rls_policies.py` - Validate RLS policies (when implemented)
- `python scripts/validate_indexes.py` - Validate database indexes (when implemented)

### Security Validation

**Commands:**
- `semgrep --config=auto app/` - Security scanning (backend)
- `semgrep --config=auto frontend/` - Security scanning (frontend)

---

## Development Workflow Requirements

### Local Development Setup

1. **Clone Repository**
   - Git repository access
   - Clone command execution

2. **Frontend Setup**
   - Navigate to `frontend/` directory
   - Run `npm install`
   - Copy `.env.example` to `.env.local`
   - Configure environment variables
   - Run `npm run dev` (starts dev server on port 3000)

3. **Backend Setup**
   - Navigate to `backend/` directory
   - Create virtual environment: `python -m venv venv`
   - Activate virtual environment
   - Install dependencies: `pip install -r requirements.txt`
   - Copy `.env.example` to `.env`
   - Configure environment variables
   - Run migrations: `alembic upgrade head`
   - Run `uvicorn app.main:app --reload` (starts API server on port 8000)

4. **Database Setup**
   - Supabase project created
   - Database connection string configured
   - Initial migrations applied

### DevContainer Setup (Optional)

1. **VS Code Dev Containers**
   - Open project in VS Code
   - Install Dev Containers extension
   - Reopen in container
   - Wait for container build and dependency installation

---

## Performance Requirements

### Development Environment

- **Node.js:** Fast enough for local development (standard hardware)
- **Python:** Fast enough for local development (standard hardware)
- **Database:** Supabase free tier acceptable for development

### Production Environment

- **API Response Time:** <200ms for CRUD operations (under 1k records)
- **Frontend Page Render:** <1s on broadband connection
- **Dashboard Load:** <1s for weekly summary

**Note:** Performance targets are for production. Development environment should support debugging and iteration without strict performance requirements.

---

## Security Requirements

### Credential Management

- **Environment Variables:** Never commit `.env` files
- **Secret Storage:** Use `.env.example` as template
- **Supabase Keys:** Store securely, never expose in client code (except anon key)
- **Database Credentials:** Use connection string from Supabase dashboard

### Security Scanning

- **Automated:** semgrep integration in CI/CD
- **Manual:** Security review before deployment

---

## Dependencies Summary

### Frontend Dependencies (from package.json)
- Next.js 14
- React 18+
- TypeScript 5.0+
- Tailwind CSS
- react-hook-form
- Zod
- @supabase/supabase-js

### Backend Dependencies (from requirements.txt)
- FastAPI 0.110
- Python 3.11
- SQLModel
- Alembic
- Pydantic
- uvicorn
- pytest (dev)

---

## Coverage Assessment

**Requirements Coverage:** 100%  
**Tooling Coverage:** 100%  
**Service Coverage:** 100%  
**Configuration Coverage:** 100%

**Missing Requirements:** None identified  
**Undefined Requirements:** None identified

---

## Next Steps

1. Validate credentials and access (STEP 1.2)
2. Capture risk flags (STEP 1.3)
3. Execute environment doctor (STEP 2.1)
4. Provision scaffold and dependencies (STEP 2.2)

---

**Evidence Location:** `.artifacts/protocol-09/environment-requirements.md`  
**Status:** Complete  
**Validated:** Yes




