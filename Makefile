.PHONY: setup build up down restart logs clean help

help:
	@echo "Доступные команды:"
	@echo "  make setup       - Полная установка и запуск проекта (первый запуск)"
	@echo "  make build       - Сборка Docker образов"
	@echo "  make up          - Запуск контейнеров"
	@echo "  make down        - Остановка контейнеров"
	@echo "  make restart     - Перезапуск контейнеров"
	@echo "  make logs        - Просмотр логов всех сервисов"
	@echo "  make logs-backend - Просмотр логов бэкенда"
	@echo "  make logs-frontend - Просмотр логов фронтенда"
	@echo "  make clean       - Очистка всех данных (volumes, images)"
	@echo "  make shell-backend - Войти в shell контейнера бэкенда"
	@echo "  make shell-db    - Войти в PostgreSQL"

setup:
	@echo "🚀 Начинаем установку проекта Streets of Russia..."
	@if [ ! -f .env ]; then \
		echo "📝 Создаем .env файл из .env.example..."; \
		cp .env.example .env; \
		echo "✅ Файл .env создан. При необходимости отредактируйте его."; \
	else \
		echo "ℹ️  Файл .env уже существует."; \
	fi
	@echo "🏗️  Собираем Docker образы..."
	docker-compose build
	@echo "🎯 Запускаем контейнеры..."
	docker-compose up -d
	@echo ""
	@echo "⏳ Ожидание запуска сервисов..."
	@sleep 30
	@echo ""
	@echo "✅ Проект успешно запущен!"
	@echo ""
	@echo "📍 Доступные адреса:"
	@echo "   🎨 Frontend: http://localhost:3000"
	@echo "   ⚙️  Backend API (Swagger): http://localhost:8000/swagger/"
	@echo "   🔧 Admin Panel: http://localhost:8000/admin/"
	@echo ""
	@echo "📊 Просмотр логов: make logs"
	@echo "🛑 Остановка: make down"

build:
	@echo "🏗️  Сборка Docker образов..."
	docker-compose build

up:
	@echo "🎯 Запуск контейнеров..."
	docker-compose up -d
	@echo "✅ Контейнеры запущены"

down:
	@echo "🛑 Остановка контейнеров..."
	docker-compose down
	@echo "✅ Контейнеры остановлены"

restart:
	@echo "🔄 Перезапуск контейнеров..."
	docker-compose restart
	@echo "✅ Контейнеры перезапущены"

logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

logs-db:
	docker-compose logs -f db

clean:
	@echo "🧹 Очистка данных проекта..."
	@read -p "Вы уверены? Это удалит все контейнеры, образы и данные (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		docker-compose down -v --rmi all; \
		echo "✅ Очистка завершена"; \
	else \
		echo "❌ Очистка отменена"; \
	fi

shell-backend:
	docker-compose exec backend sh

shell-db:
	docker-compose exec db psql -U $${POSTGRES_USER:-postgres} -d $${POSTGRES_DB:-streets_db}

migrate:
	@echo "🔄 Применение миграций..."
	docker-compose exec backend python manage.py migrate
	@echo "✅ Миграции применены"

makemigrations:
	@echo "📝 Создание миграций..."
	docker-compose exec backend python manage.py makemigrations
	@echo "✅ Миграции созданы"

createsuperuser:
	@echo "👤 Создание суперпользователя..."
	docker-compose exec backend python manage.py createsuperuser

collectstatic:
	@echo "📦 Сбор статических файлов..."
	docker-compose exec backend python manage.py collectstatic --noinput
	@echo "✅ Статика собрана"
