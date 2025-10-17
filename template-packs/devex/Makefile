.PHONY: help setup dev test lint build deploy clean

# Default target
.DEFAULT_GOAL := help

# Project variables
PROJECT_NAME := {{PROJECT_NAME}}
PYTHON := python3
NODE := node
DOCKER_COMPOSE := docker-compose
FRONTEND_DIR := frontend
BACKEND_DIR := backend

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo '${GREEN}{{PROJECT_NAME}} Makefile${NC}'
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${NC} ${GREEN}<target>${NC}'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  ${YELLOW}%-15s${NC} %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Initial project setup
	@echo "${GREEN}Setting up {{PROJECT_NAME}}...${NC}"
	@echo "${YELLOW}Installing frontend dependencies...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm install; \
	fi
	@echo "${YELLOW}Installing backend dependencies...${NC}"
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && $(PYTHON) -m venv venv && \
		. venv/bin/activate && pip install -r requirements.txt; \
	fi
	@echo "${YELLOW}Setting up environment files...${NC}"
	@if [ ! -f .env ]; then cp .env.example .env; fi
	@if [ -f "$(FRONTEND_DIR)/.env.example" ] && [ ! -f "$(FRONTEND_DIR)/.env.local" ]; then \
		cp $(FRONTEND_DIR)/.env.example $(FRONTEND_DIR)/.env.local; \
	fi
	@if [ -f "$(BACKEND_DIR)/.env.example" ] && [ ! -f "$(BACKEND_DIR)/.env" ]; then \
		cp $(BACKEND_DIR)/.env.example $(BACKEND_DIR)/.env; \
	fi
	@echo "${GREEN}Setup complete!${NC}"

dev: ## Start development environment
	@echo "${GREEN}Starting development environment...${NC}"
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml up -d
	@echo "${YELLOW}Waiting for services to be ready...${NC}"
	@sleep 5
	@echo "${GREEN}Services running:${NC}"
	@echo "  Frontend: http://localhost:3000"
	@echo "  Backend:  http://localhost:8000"
	@echo "  API Docs: http://localhost:8000/api/docs"
	@echo "  PgAdmin:  http://localhost:5050"
	@echo "  MailHog:  http://localhost:8025"

dev-logs: ## Show development logs
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml logs -f

dev-stop: ## Stop development environment
	@echo "${YELLOW}Stopping development environment...${NC}"
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml down

dev-restart: ## Restart development environment
	@make dev-stop
	@make dev

test: ## Run all tests
	@echo "${GREEN}Running tests...${NC}"
	@echo "${YELLOW}Running frontend tests...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm test; \
	fi
	@echo "${YELLOW}Running backend tests...${NC}"
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && pytest; \
	fi

test-frontend: ## Run frontend tests
	@echo "${GREEN}Running frontend tests...${NC}"
	@cd $(FRONTEND_DIR) && npm test

test-backend: ## Run backend tests
	@echo "${GREEN}Running backend tests...${NC}"
	@cd $(BACKEND_DIR) && . venv/bin/activate && pytest

test-coverage: ## Run tests with coverage
	@echo "${GREEN}Running tests with coverage...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm run test:coverage; \
	fi
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && pytest --cov=app tests/; \
	fi

lint: ## Run linters
	@echo "${GREEN}Running linters...${NC}"
	@echo "${YELLOW}Linting frontend...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm run lint; \
	fi
	@echo "${YELLOW}Linting backend...${NC}"
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && \
		black --check . && \
		flake8 && \
		mypy app; \
	fi

lint-fix: ## Fix linting issues
	@echo "${GREEN}Fixing linting issues...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm run lint -- --fix; \
	fi
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && black .; \
	fi

format: lint-fix ## Format code (alias for lint-fix)

build: ## Build for production
	@echo "${GREEN}Building for production...${NC}"
	@echo "${YELLOW}Building frontend...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm run build; \
	fi
	@echo "${YELLOW}Building backend...${NC}"
	@if [ -d "$(BACKEND_DIR)" ]; then \
		docker build -t $(PROJECT_NAME)-backend $(BACKEND_DIR); \
	fi
	@echo "${GREEN}Build complete!${NC}"

build-images: ## Build Docker images
	@echo "${GREEN}Building Docker images...${NC}"
	$(DOCKER_COMPOSE) -f docker-compose.yml build

db-migrate: ## Run database migrations
	@echo "${GREEN}Running database migrations...${NC}"
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && alembic upgrade head; \
	fi

db-rollback: ## Rollback database migration
	@echo "${YELLOW}Rolling back database migration...${NC}"
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && alembic downgrade -1; \
	fi

db-reset: ## Reset database
	@echo "${RED}Resetting database...${NC}"
	@echo "${YELLOW}This will delete all data. Are you sure? [y/N]${NC}"
	@read -r response; \
	if [ "$$response" = "y" ]; then \
		$(DOCKER_COMPOSE) -f docker-compose.dev.yml down -v; \
		$(DOCKER_COMPOSE) -f docker-compose.dev.yml up -d db; \
		sleep 5; \
		make db-migrate; \
		echo "${GREEN}Database reset complete!${NC}"; \
	else \
		echo "${YELLOW}Database reset cancelled.${NC}"; \
	fi

security-check: ## Run security checks
	@echo "${GREEN}Running security checks...${NC}"
	@if [ -d "$(FRONTEND_DIR)" ]; then \
		cd $(FRONTEND_DIR) && npm audit; \
	fi
	@if [ -d "$(BACKEND_DIR)" ]; then \
		cd $(BACKEND_DIR) && . venv/bin/activate && \
		pip-audit && \
		bandit -r app/; \
	fi

deploy-staging: ## Deploy to staging
	@echo "${GREEN}Deploying to staging...${NC}"
	@echo "${YELLOW}Running pre-deployment checks...${NC}"
	@make lint
	@make test
	@make build
	@echo "${GREEN}Deployment to staging complete!${NC}"

deploy-production: ## Deploy to production
	@echo "${RED}Deploying to production...${NC}"
	@echo "${YELLOW}This will deploy to production. Are you sure? [y/N]${NC}"
	@read -r response; \
	if [ "$$response" = "y" ]; then \
		make lint && \
		make test && \
		make build && \
		echo "${GREEN}Deployment to production complete!${NC}"; \
	else \
		echo "${YELLOW}Production deployment cancelled.${NC}"; \
	fi

clean: ## Clean build artifacts
	@echo "${GREEN}Cleaning build artifacts...${NC}"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".next" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "${GREEN}Clean complete!${NC}"

clean-all: clean ## Clean everything including Docker
	@echo "${RED}Cleaning all artifacts and Docker resources...${NC}"
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml down -v --remove-orphans
	docker system prune -af --volumes
	@echo "${GREEN}Deep clean complete!${NC}"

logs: ## Show all logs
	@if [ -f "$(BACKEND_DIR)/app.log" ]; then \
		tail -f $(BACKEND_DIR)/app.log; \
	else \
		echo "${YELLOW}No log files found.${NC}"; \
	fi

shell-backend: ## Open backend shell
	@echo "${GREEN}Opening backend shell...${NC}"
	@cd $(BACKEND_DIR) && . venv/bin/activate && python

shell-db: ## Open database shell
	@echo "${GREEN}Opening database shell...${NC}"
	docker exec -it $(PROJECT_NAME)_postgres psql -U postgres -d $(PROJECT_NAME)

shell-redis: ## Open Redis CLI
	@echo "${GREEN}Opening Redis CLI...${NC}"
	docker exec -it $(PROJECT_NAME)_redis redis-cli

backup: ## Backup database
	@echo "${GREEN}Backing up database...${NC}"
	@mkdir -p backups
	docker exec $(PROJECT_NAME)_postgres pg_dump -U postgres $(PROJECT_NAME) | gzip > backups/$(PROJECT_NAME)_$(shell date +%Y%m%d_%H%M%S).sql.gz
	@echo "${GREEN}Backup complete!${NC}"

restore: ## Restore database from backup
	@echo "${YELLOW}Available backups:${NC}"
	@ls -la backups/*.sql.gz
	@echo ""
	@echo "${YELLOW}Enter backup filename to restore:${NC}"
	@read -r filename; \
	if [ -f "backups/$$filename" ]; then \
		gunzip -c backups/$$filename | docker exec -i $(PROJECT_NAME)_postgres psql -U postgres $(PROJECT_NAME); \
		echo "${GREEN}Restore complete!${NC}"; \
	else \
		echo "${RED}Backup file not found!${NC}"; \
	fi