#!/bin/bash
# Initial setup script for {{PROJECT_NAME}} Django backend

set -e

echo "🚀 Setting up {{PROJECT_NAME}} Django backend..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.11"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)"; then
    echo "❌ Python 3.11+ is required. Current version: $python_version"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Copy .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your configuration"
fi

# Check PostgreSQL
if command -v psql &> /dev/null; then
    echo "✅ PostgreSQL is installed"
else
    echo "⚠️  PostgreSQL is not installed. Please install it to continue."
fi

# Check Redis
if command -v redis-cli &> /dev/null; then
    echo "✅ Redis is installed"
else
    echo "⚠️  Redis is not installed. Please install it for caching and Celery."
fi

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

# Create superuser
echo "👤 Create a superuser account:"
python manage.py createsuperuser

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Setup complete!"
echo ""
echo "To start the development server:"
echo "  1. Start Redis: redis-server"
echo "  2. Start Celery: celery -A {{PROJECT_NAME}} worker --loglevel=info"
echo "  3. Start Django: python manage.py runserver"
echo ""
echo "Visit http://localhost:8000 to see your API"