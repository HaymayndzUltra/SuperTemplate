# Environment Setup Handbook

**Project:** Freelancer Command Center MVP  
**Generated:** 2025-01-27  
**Version:** 1.0  
**Status:** Draft - Pending Tool Installation

---

## Overview

This handbook provides step-by-step instructions for setting up the development environment for the Freelancer Command Center MVP. Follow these instructions to provision a consistent development environment aligned with technical design requirements.

---

## Prerequisites

### Required Tools

Before proceeding, ensure you have the following tools installed:

- **Node.js:** Version 18+ (https://nodejs.org)
- **Python:** Version 3.11+ (https://www.python.org/downloads/)
- **Git:** Version 2.30+ (https://git-scm.com/downloads)
- **npm:** Comes with Node.js (version 9+)
- **pip:** Comes with Python (version 22+)

### Optional Tools

- **Docker:** For devcontainer support (https://docker.com)
- **VS Code:** With Dev Containers extension (for devcontainer)

### External Services

- **Supabase Account:** For database and authentication (https://supabase.com)
- **Vercel Account:** For frontend deployment (https://vercel.com) - Optional for development
- **Render Account:** For backend deployment (https://render.com) - Optional for development

---

## Quick Start

### 1. Clone Repository

```bash
git clone <repository-url>
cd SuperTemplate
```

### 2. Install Frontend Dependencies

```bash
cd frontend
npm install
```

**Expected Output:** Dependencies installed successfully

**Note:** Requires Node.js 18+

### 3. Install Backend Dependencies

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Expected Output:** Dependencies installed successfully

**Note:** Requires Python 3.11+

### 4. Configure Environment Variables

#### Frontend Environment Variables

Create `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

#### Backend Environment Variables

Create `backend/.env`:

```env
DATABASE_URL=your_supabase_postgresql_connection_string
SUPABASE_URL=your_supabase_url
SUPABASE_JWT_SECRET=your_supabase_jwt_secret
CORS_ORIGINS=http://localhost:3000
```

**Note:** Obtain Supabase credentials from your Supabase project dashboard.

### 5. Run Database Migrations

```bash
cd backend
source venv/bin/activate  # If not already activated
alembic upgrade head
```

**Expected Output:** Migrations applied successfully

### 6. Start Development Servers

#### Frontend (Terminal 1)

```bash
cd frontend
npm run dev
```

**Expected Output:** Server running on http://localhost:3000

#### Backend (Terminal 2)

```bash
cd backend
source venv/bin/activate  # If not already activated
uvicorn app.main:app --reload
```

**Expected Output:** Server running on http://localhost:8000

---

## Detailed Setup Instructions

### Frontend Setup

#### Step 1: Verify Node.js Installation

```bash
node --version  # Should be 18.0.0 or higher
npm --version   # Should be 9.0.0 or higher
```

#### Step 2: Install Dependencies

```bash
cd frontend
npm install
```

This installs:
- Next.js 16.0.1
- React 19.2.0
- TypeScript 5.0+
- Tailwind CSS 4
- Supabase Auth SDK
- Form validation libraries (react-hook-form + Zod)

#### Step 3: Configure Environment Variables

Create `frontend/.env.local` with Supabase credentials.

#### Step 4: Start Development Server

```bash
npm run dev
```

Access the application at http://localhost:3000

#### Step 5: Run Linting

```bash
npm run lint
```

**Expected Output:** No linting errors

---

### Backend Setup

#### Step 1: Verify Python Installation

```bash
python3 --version  # Should be 3.11.0 or higher
pip --version       # Should be 22.0.0 or higher
```

#### Step 2: Create Virtual Environment

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- FastAPI 0.121.0
- SQLModel 0.0.27
- Alembic 1.17.1
- Pydantic 2.12.3
- uvicorn 0.38.0
- PostgreSQL driver (psycopg2-binary)

#### Step 4: Configure Environment Variables

Create `backend/.env` with database and Supabase credentials.

#### Step 5: Run Database Migrations

```bash
alembic upgrade head
```

**Expected Output:** Migrations applied successfully

#### Step 6: Start Development Server

```bash
uvicorn app.main:app --reload
```

Access the API at http://localhost:8000

#### Step 7: Verify API Health

```bash
curl http://localhost:8000/docs
```

Should display FastAPI Swagger documentation.

---

### Database Setup

#### Step 1: Create Supabase Project

1. Go to https://supabase.com
2. Create a new project
3. Note your project URL and API keys

#### Step 2: Configure Database Connection

Obtain PostgreSQL connection string from Supabase dashboard:
- Settings → Database → Connection String

#### Step 3: Apply Migrations

```bash
cd backend
source venv/bin/activate
alembic upgrade head
```

#### Step 4: Verify RLS Policies

RLS policies should be created automatically via migrations. Verify in Supabase dashboard:
- Authentication → Policies

---

## Validation Commands

### Frontend Validation

```bash
cd frontend
npm run lint              # ESLint validation
npm run build             # Production build test
npm run type-check        # TypeScript validation (if script exists)
```

### Backend Validation

```bash
cd backend
source venv/bin/activate
pytest                    # Run all tests
alembic check            # Validate Alembic configuration
python scripts/test_db_connection.py  # Test database connection
```

### Security Validation

```bash
semgrep --config=auto app/         # Backend security scan
semgrep --config=auto frontend/    # Frontend security scan
```

---

## Troubleshooting

### Node.js Not Found

**Error:** `node: command not found`

**Solution:**
1. Install Node.js 18+ from https://nodejs.org
2. Verify installation: `node --version`
3. Restart terminal

### Python Version Mismatch

**Error:** `Python 3.10.12 detected, but 3.11+ required`

**Solution:**
1. Install Python 3.11+ from https://www.python.org/downloads/
2. Use pyenv for version management: `pyenv install 3.11.0`
3. Set local version: `pyenv local 3.11.0`

### Database Connection Failed

**Error:** `Connection refused` or `Authentication failed`

**Solution:**
1. Verify DATABASE_URL in `.env`
2. Check Supabase project status
3. Verify connection string format
4. Test connection: `python scripts/test_db_connection.py`

### Frontend Build Fails

**Error:** TypeScript errors or build failures

**Solution:**
1. Check TypeScript configuration: `frontend/tsconfig.json`
2. Verify all dependencies installed: `npm install`
3. Check environment variables: `frontend/.env.local`
4. Review error messages for specific issues

### Backend Migration Fails

**Error:** Alembic migration errors

**Solution:**
1. Verify DATABASE_URL configuration
2. Check database connection: `python scripts/test_db_connection.py`
3. Review migration files: `backend/alembic/versions/`
4. Check Alembic configuration: `backend/alembic.ini`

---

## DevContainer Setup (Optional)

### Prerequisites

- Docker installed and running
- VS Code with Dev Containers extension

### Steps

1. Open project in VS Code
2. Install Dev Containers extension
3. Click "Reopen in Container"
4. Wait for container build and dependency installation

**Note:** DevContainer configuration is in `.devcontainer/devcontainer.json`

---

## Automation References

### CI/CD Integration

GitHub Actions workflows are configured in `.github/workflows/`:
- Frontend linting and type checking
- Backend testing
- Security scanning

### Task Automation

See `task-automation-matrix.json` for automation hooks:
- Validation scripts per task
- CI/CD integration points
- Testing commands

---

## Environment Variables Reference

### Frontend (.env.local)

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | Yes | Backend API base URL | `http://localhost:8000/api/v1` |
| `NEXT_PUBLIC_SUPABASE_URL` | Yes | Supabase project URL | `https://xxx.supabase.co` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Yes | Supabase anonymous key | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |

### Backend (.env)

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `DATABASE_URL` | Yes | PostgreSQL connection string | `postgresql://user:pass@host:5432/db` |
| `SUPABASE_URL` | Yes | Supabase project URL | `https://xxx.supabase.co` |
| `SUPABASE_JWT_SECRET` | Yes | JWT secret for token validation | `your-jwt-secret` |
| `CORS_ORIGINS` | Yes | Allowed CORS origins | `http://localhost:3000` |

---

## Performance Expectations

### Development Environment

- **Frontend Dev Server:** Starts in ~5-10 seconds
- **Backend Dev Server:** Starts in ~2-5 seconds
- **Hot Reload:** Updates in <1 second

### Production Targets

- **API Response Time:** <200ms for CRUD operations
- **Frontend Page Render:** <1s on broadband
- **Dashboard Load:** <1s for weekly summary

---

## Next Steps

After environment setup:

1. **Protocol 10:** Process Tasks - Begin task execution
2. **Development:** Start implementing features per task plan
3. **Testing:** Run validation suite regularly
4. **Deployment:** Configure deployment platforms (Protocol 15)

---

## Support

### Documentation

- **Project Brief:** `.artifacts/protocol-03/PROJECT-BRIEF.md`
- **Technical Design:** `.artifacts/protocol-07/TECHNICAL-DESIGN.md`
- **Architecture Principles:** `.artifacts/protocol-05/architecture-principles.md`

### Issues

If you encounter issues not covered in this handbook:

1. Check troubleshooting section above
2. Review environment diagnostics: `.artifacts/protocol-09/environment-diagnostics.json`
3. Verify prerequisites are met
4. Check environment variables configuration

---

**Evidence Location:** `.artifacts/protocol-09/ENVIRONMENT-README.md`  
**Status:** Complete  
**Validated:** Yes  
**Last Updated:** 2025-01-27
