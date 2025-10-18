#!/bin/bash

# GitHub Token Setup Script
# This script helps you set up GitHub authentication for the SuperTemplate repository

echo "🔐 GitHub Token Setup for SuperTemplate Repository"
echo "=================================================="
echo ""

# Check if .env file exists
if [ -f ".env" ]; then
    echo "✅ .env file found"
else
    echo "❌ .env file not found. Creating one..."
    cat > .env << 'EOF'
# GitHub Authentication Environment Variables
GH_SUPER=your_github_token_here
GITHUB_TOKEN=your_github_token_here
GITHUB_API_URL=https://api.github.com
GITHUB_OWNER=HaymayndzUltra
GITHUB_REPO=SuperTemplate
EOF
    echo "✅ .env file created"
fi

echo ""
echo "📋 Instructions to get your GitHub Personal Access Token:"
echo "1. Go to GitHub.com → Settings → Developer settings → Personal access tokens"
echo "2. Click 'Generate new token (classic)'"
echo "3. Give it a name like 'SuperTemplate Access'"
echo "4. Select these scopes:"
echo "   - repo (Full control of private repositories)"
echo "   - read:org (Read org and team membership)"
echo "   - read:user (Read user profile data)"
echo "5. Click 'Generate token'"
echo "6. Copy the token (it won't be shown again!)"
echo ""

# Function to set token
set_token() {
    if [ -z "$1" ]; then
        echo "❌ No token provided"
        return 1
    fi
    
    # Update .env file
    sed -i "s/GH_SUPER=.*/GH_SUPER=$1/" .env
    sed -i "s/GITHUB_TOKEN=.*/GITHUB_TOKEN=$1/" .env
    
    # Set environment variable for current session
    export GH_SUPER="$1"
    export GITHUB_TOKEN="$1"
    
    echo "✅ Token set successfully!"
    echo "✅ Environment variables updated"
    echo "✅ Token added to .env file"
}

# Check if token is provided as argument
if [ $# -eq 1 ]; then
    echo "Setting token from command line argument..."
    set_token "$1"
else
    echo "To set your token, run:"
    echo "  ./setup-github-token.sh YOUR_TOKEN_HERE"
    echo ""
    echo "Or manually edit the .env file and replace 'your_github_token_here' with your actual token"
fi

echo ""
echo "🔍 To test your token, run:"
echo "  curl -H \"Authorization: token \$GH_SUPER\" https://api.github.com/user"
echo ""
echo "📝 Remember: Never commit your .env file with real tokens!"
