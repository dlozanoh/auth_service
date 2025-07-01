# Makefile for Authentication Service with JWT, MySQL, and Redis

PROJECT_NAME=auth_service
COMPOSE=docker-compose
PYTHON=docker-compose exec app python

# 🐳 Docker commands
up:
	@echo "🚀 Starting $(PROJECT_NAME) services..."
	$(COMPOSE) up --build

down:
	@echo "🛑 Stopping $(PROJECT_NAME) services..."
	$(COMPOSE) down

restart: down up

logs:
	$(COMPOSE) logs -f

# 🧪 Testing & Formatting
test:
	@echo "🧪 Running tests..."
	$(PYTHON) -m unittest discover -s app/tests

format:
	@echo "🎨 Formatting with Black..."
	$(PYTHON) -m black app/

lint:
	@echo "🔍 Linting with flake8..."
	$(PYTHON) -m flake8 app/

# 🛠️ DB / Redis
connect_postgres:
	@echo "🐬 Connecting to PostgreSQL CLI..."
	docker-compose exec db psql -U <username> -d <database>

redis-cli:
	@echo "🧠 Connecting to Redis CLI..."
	docker exec -it $(PROJECT_NAME)-redis-1 redis-cli

# ⚙️ Misc
shell:
	@echo "🐚 Dropping into shell..."
	$(COMPOSE) exec app sh

help:
	@echo ""
	@echo "Makefile commands for $(PROJECT_NAME):"
	@echo "  up           - Build and start all services"
	@echo "  down         - Stop all services"
	@echo "  restart      - Restart services"
	@echo "  logs         - Tail logs"
	@echo "  test         - Run unit tests"
	@echo "  format       - Run Black formatter"
	@echo "  lint         - Run flake8 linter"
	@echo "  mysql        - Open MySQL CLI"
	@echo "  redis-cli    - Open Redis CLI"
	@echo "  shell        - Open shell in app container"
	@echo ""
