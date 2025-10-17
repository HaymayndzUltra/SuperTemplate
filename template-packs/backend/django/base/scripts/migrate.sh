#!/bin/bash
# Migration helper script for {{PROJECT_NAME}} Django backend

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Function to show usage
usage() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  make         Create new migrations"
    echo "  apply        Apply pending migrations"
    echo "  show         Show migration status"
    echo "  rollback     Rollback to previous migration"
    echo "  reset        Reset all migrations (WARNING: destructive)"
    echo "  fake         Mark migrations as applied without running them"
    echo ""
    exit 1
}

# Check if Django is available
if ! python -c "import django" 2>/dev/null; then
    echo -e "${RED}❌ Django is not installed. Run setup.sh first.${NC}"
    exit 1
fi

case "$1" in
    make)
        echo -e "${GREEN}Creating new migrations...${NC}"
        python manage.py makemigrations
        echo -e "${YELLOW}Review the migrations before applying them!${NC}"
        ;;
    
    apply)
        echo -e "${GREEN}Applying pending migrations...${NC}"
        python manage.py migrate
        echo -e "${GREEN}✅ Migrations applied successfully${NC}"
        ;;
    
    show)
        echo -e "${GREEN}Migration status:${NC}"
        python manage.py showmigrations
        ;;
    
    rollback)
        if [ -z "$2" ]; then
            echo -e "${RED}Please specify the app and migration to rollback to${NC}"
            echo "Example: $0 rollback authentication 0001"
            exit 1
        fi
        echo -e "${YELLOW}Rolling back $2 to migration $3...${NC}"
        python manage.py migrate $2 $3
        ;;
    
    reset)
        echo -e "${RED}WARNING: This will delete all data in your database!${NC}"
        read -p "Are you sure? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            echo -e "${YELLOW}Resetting all migrations...${NC}"
            
            # Find all migration folders and delete migration files
            find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
            find . -path "*/migrations/*.pyc" -delete
            
            # Drop and recreate database
            echo -e "${YELLOW}Recreating database...${NC}"
            python manage.py dbshell << EOF
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
EOF
            
            # Create fresh migrations
            python manage.py makemigrations
            python manage.py migrate
            
            echo -e "${GREEN}✅ Database reset complete${NC}"
        else
            echo -e "${YELLOW}Reset cancelled${NC}"
        fi
        ;;
    
    fake)
        if [ -z "$2" ]; then
            echo -e "${YELLOW}Marking all migrations as applied...${NC}"
            python manage.py migrate --fake
        else
            echo -e "${YELLOW}Marking $2 migrations as applied...${NC}"
            python manage.py migrate $2 --fake
        fi
        echo -e "${GREEN}✅ Migrations marked as applied${NC}"
        ;;
    
    *)
        usage
        ;;
esac