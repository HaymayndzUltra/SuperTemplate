.PHONY: help build run test clean deps lint fmt migrate migrate-down docker-build docker-run

# Variables
APP_NAME={{PROJECT_NAME}}
BUILD_DIR=./build
MAIN_FILE=main.go
DOCKER_IMAGE={{PROJECT_NAME}}-backend

## help: Show this help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

## deps: Download dependencies
deps:
	@echo "Downloading dependencies..."
	@go mod download
	@go mod tidy

## build: Build the application
build: deps
	@echo "Building $(APP_NAME)..."
	@go build -o $(BUILD_DIR)/$(APP_NAME) $(MAIN_FILE)

## run: Run the application
run: deps
	@echo "Running $(APP_NAME)..."
	@go run $(MAIN_FILE)

## test: Run tests
test:
	@echo "Running tests..."
	@go test -v -cover ./...

## test-coverage: Run tests with coverage report
test-coverage:
	@echo "Running tests with coverage..."
	@go test -v -coverprofile=coverage.out ./...
	@go tool cover -html=coverage.out -o coverage.html
	@echo "Coverage report generated: coverage.html"

## lint: Run linter
lint:
	@echo "Running linter..."
	@golangci-lint run ./...

## fmt: Format code
fmt:
	@echo "Formatting code..."
	@go fmt ./...
	@gofmt -s -w .

## clean: Clean build artifacts
clean:
	@echo "Cleaning..."
	@rm -rf $(BUILD_DIR)
	@rm -f coverage.out coverage.html

## migrate: Run database migrations
migrate:
	@echo "Running migrations..."
	@go run main.go migrate up

## migrate-down: Rollback database migrations
migrate-down:
	@echo "Rolling back migrations..."
	@go run main.go migrate down

## docker-build: Build Docker image
docker-build:
	@echo "Building Docker image..."
	@docker build -t $(DOCKER_IMAGE) .

## docker-run: Run application in Docker
docker-run:
	@echo "Running Docker container..."
	@docker run -p 8000:8000 --env-file .env $(DOCKER_IMAGE)

## dev: Run in development mode with hot reload
dev:
	@echo "Running in development mode..."
	@air

## seed: Seed the database with sample data
seed:
	@echo "Seeding database..."
	@go run main.go seed

## setup: Initial project setup
setup:
	@echo "Setting up project..."
	@cp .env.example .env
	@go mod download
	@echo "Please edit .env file with your configuration"
	@echo "Run 'make migrate' to set up the database"