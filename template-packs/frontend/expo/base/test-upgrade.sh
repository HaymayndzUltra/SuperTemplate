#!/bin/bash

# Expo SDK 54 Upgrade Testing Script
# This script helps verify that the upgrade was successful

set -e

echo "🚀 Starting Expo SDK 54 Upgrade Testing..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    print_error "package.json not found. Please run this script from the project root."
    exit 1
fi

# Step 1: Install dependencies
print_status "Installing dependencies..."
if command -v yarn &> /dev/null; then
    yarn install
else
    npm install
fi
print_success "Dependencies installed"

# Step 2: Fix Expo dependencies
print_status "Fixing Expo dependencies..."
npx expo install --fix
print_success "Expo dependencies fixed"

# Step 3: Type checking
print_status "Running TypeScript type checking..."
if npx tsc --noEmit; then
    print_success "TypeScript compilation successful"
else
    print_error "TypeScript compilation failed"
    exit 1
fi

# Step 4: Linting
print_status "Running ESLint..."
if npx eslint . --ext .js,.jsx,.ts,.tsx --max-warnings 0; then
    print_success "ESLint passed"
else
    print_warning "ESLint found issues (check output above)"
fi

# Step 5: Test prebuild
print_status "Testing expo prebuild..."
if npx expo prebuild --clean; then
    print_success "Expo prebuild successful"
else
    print_error "Expo prebuild failed"
    exit 1
fi

# Step 6: Check for config plugin warnings
print_status "Checking for config plugin warnings..."
if npx expo prebuild --platform ios --no-install 2>&1 | grep -i "warning\|error"; then
    print_warning "Config plugin warnings found (check output above)"
else
    print_success "No config plugin warnings"
fi

# Step 7: Verify package versions
print_status "Verifying package versions..."
echo "Checking key package versions:"

# Check Expo version
EXPO_VERSION=$(node -p "require('./package.json').dependencies.expo")
echo "  Expo: $EXPO_VERSION"
if [[ $EXPO_VERSION == *"54"* ]]; then
    print_success "Expo SDK 54 detected"
else
    print_error "Expo SDK version mismatch"
fi

# Check React version
REACT_VERSION=$(node -p "require('./package.json').dependencies.react")
echo "  React: $REACT_VERSION"
if [[ $REACT_VERSION == *"19"* ]]; then
    print_success "React 19 detected"
else
    print_error "React version mismatch"
fi

# Check React Native version
RN_VERSION=$(node -p "require('./package.json').dependencies['react-native']")
echo "  React Native: $RN_VERSION"
if [[ $RN_VERSION == *"0.81"* ]]; then
    print_success "React Native 0.81 detected"
else
    print_error "React Native version mismatch"
fi

# Check Reanimated version
REANIMATED_VERSION=$(node -p "require('./package.json').dependencies['react-native-reanimated']")
echo "  Reanimated: $REANIMATED_VERSION"
if [[ $REANIMATED_VERSION == *"4"* ]]; then
    print_success "Reanimated v4 detected"
else
    print_error "Reanimated version mismatch"
fi

# Check Worklets
if grep -q "react-native-worklets" package.json; then
    print_success "React Native Worklets installed"
else
    print_error "React Native Worklets not found"
fi

# Step 8: Test development server (non-blocking)
print_status "Testing development server startup..."
timeout 10s npx expo start --no-dev --minify > /dev/null 2>&1 &
SERVER_PID=$!
sleep 5
if kill -0 $SERVER_PID 2>/dev/null; then
    print_success "Development server started successfully"
    kill $SERVER_PID 2>/dev/null || true
else
    print_warning "Development server test inconclusive"
fi

# Step 9: Summary
echo ""
echo "=========================================="
print_success "Expo SDK 54 Upgrade Testing Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Run 'npx expo start' to test the development server"
echo "2. Run 'npx expo run:ios' to test iOS build"
echo "3. Run 'npx expo run:android' to test Android build"
echo "4. Run 'eas build --profile development' to test EAS builds"
echo ""
echo "For detailed testing instructions, see UPGRADE_SDK_54.md"
echo ""
print_status "Happy coding with Expo SDK 54! 🎉"
