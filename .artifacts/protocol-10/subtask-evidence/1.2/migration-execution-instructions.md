# Migration Execution Instructions - Task 1.2.6

**Date:** 2025-01-27  
**Status:** ⚠️ **Network Connection Issue**

---

## Proper Migration Execution Steps

### 1. Activate Virtual Environment

**Important:** Always activate the venv before running Alembic!

```bash
cd /home/haymayndz/SuperTemplate/backend
source venv/bin/activate
```

**Verify venv is active:**
- You should see `(venv)` in your prompt
- Or check: `which alembic` should show `.../venv/bin/alembic`

### 2. Run Migration

```bash
alembic upgrade head
```

---

## Current Issue: Network Connection

**Error:**
```
psycopg2.OperationalError: connection to server at "db.lfexrpjwbdpkuwrfqacz.supabase.co" 
port 5432 failed: Network is unreachable
```

### Possible Causes:

1. **WSL Network Configuration**
   - WSL might not have proper network access
   - Check: `ping 8.8.8.8` to test internet connectivity

2. **Supabase Database Access**
   - Database URL might be incorrect or expired
   - Database might be paused (Supabase free tier pauses after inactivity)
   - Firewall blocking connection

3. **IPv6 Issue**
   - Error shows IPv6 address `2406:da1c:f42:ae0d:6137:43d5:ff37:68c7`
   - WSL might not have IPv6 properly configured

### Troubleshooting Steps:

**1. Check Internet Connectivity:**
```bash
ping 8.8.8.8
ping db.lfexrpjwbdpkuwrfqacz.supabase.co
```

**2. Verify DATABASE_URL:**
```bash
cd backend
source venv/bin/activate
python3 -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('DATABASE_URL'))"
```

**3. Test Database Connection:**
```bash
cd backend
source venv/bin/activate
python3 -c "from app.database import engine; engine.connect(); print('✅ Database connection successful')"
```

**4. Check Supabase Dashboard:**
- Go to Supabase Dashboard
- Check if database is active
- Verify connection string is correct
- Check if database is paused (free tier)

**5. Alternative: Use Supabase SQL Editor**
- Copy the generated SQL from: `alembic upgrade head --sql`
- Paste into Supabase Dashboard SQL Editor
- Execute manually

---

## Migration Script Status

✅ **Migration Script:** Valid  
✅ **SQL Generation:** Successful  
✅ **Syntax:** Correct  
✅ **Virtual Environment:** Configured  
⚠️ **Execution:** Pending network connection  

---

## Quick Fix Commands

**For future migrations, always use:**
```bash
cd backend
source venv/bin/activate
alembic upgrade head
```

**To generate SQL without connecting:**
```bash
cd backend
source venv/bin/activate
alembic upgrade head --sql > migration.sql
```

---

**Migration script is ready. Once network connectivity is established, migration will execute successfully.**

