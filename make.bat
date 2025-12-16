@echo off
REM Windows batch script for Streets of Russia project

if "%1"=="" goto help
if "%1"=="setup" goto setup
if "%1"=="build" goto build
if "%1"=="up" goto up
if "%1"=="down" goto down
if "%1"=="restart" goto restart
if "%1"=="logs" goto logs
if "%1"=="logs-backend" goto logs-backend
if "%1"=="logs-frontend" goto logs-frontend
if "%1"=="logs-db" goto logs-db
if "%1"=="clean" goto clean
if "%1"=="shell-backend" goto shell-backend
if "%1"=="shell-db" goto shell-db
if "%1"=="migrate" goto migrate
if "%1"=="makemigrations" goto makemigrations
if "%1"=="createsuperuser" goto createsuperuser
if "%1"=="collectstatic" goto collectstatic
goto help

:setup
echo 🚀 Начинаем установку проекта Streets of Russia...
if not exist .env (
    echo 📝 Создаем .env файл из .env.example...
    copy .env.example .env
    echo ✅ Файл .env создан. При необходимости отредактируйте его.
) else (
    echo ℹ️  Файл .env уже существует.
)
echo 🏗️  Собираем Docker образы...
docker-compose build
echo 🎯 Запускаем контейнеры...
docker-compose up -d
echo.
echo ⏳ Ожидание запуска сервисов...
timeout /t 30 /nobreak >nul
echo.
echo ✅ Проект успешно запущен!
echo.
echo 📍 Доступные адреса:
echo    🎨 Frontend: http://localhost:3000
echo    ⚙️  Backend API (Swagger): http://localhost:8000/swagger/
echo    🔧 Admin Panel: http://localhost:8000/admin/
echo.
echo 📊 Просмотр логов: make.bat logs
echo 🛑 Остановка: make.bat down
goto end

:build
echo 🏗️  Сборка Docker образов...
docker-compose build
echo ✅ Сборка завершена
goto end

:up
echo 🎯 Запуск контейнеров...
docker-compose up -d
echo ✅ Контейнеры запущены
goto end

:down
echo 🛑 Остановка контейнеров...
docker-compose down
echo ✅ Контейнеры остановлены
goto end

:restart
echo 🔄 Перезапуск контейнеров...
docker-compose restart
echo ✅ Контейнеры перезапущены
goto end

:logs
docker-compose logs -f
goto end

:logs-backend
docker-compose logs -f backend
goto end

:logs-frontend
docker-compose logs -f frontend
goto end

:logs-db
docker-compose logs -f db
goto end

:clean
echo 🧹 Очистка данных проекта...
set /p confirm="Вы уверены? Это удалит все контейнеры, образы и данные (y/N): "
if /i "%confirm%"=="y" (
    docker-compose down -v --rmi all
    echo ✅ Очистка завершена
) else (
    echo ❌ Очистка отменена
)
goto end

:shell-backend
docker-compose exec backend sh
goto end

:shell-db
docker-compose exec db psql -U postgres -d streets_db
goto end

:migrate
echo 🔄 Применение миграций...
docker-compose exec backend python manage.py migrate
echo ✅ Миграции применены
goto end

:makemigrations
echo 📝 Создание миграций...
docker-compose exec backend python manage.py makemigrations
echo ✅ Миграции созданы
goto end

:createsuperuser
echo 👤 Создание суперпользователя...
docker-compose exec backend python manage.py createsuperuser
goto end

:collectstatic
echo 📦 Сбор статических файлов...
docker-compose exec backend python manage.py collectstatic --noinput
echo ✅ Статика собрана
goto end

:help
echo Доступные команды:
echo   make.bat setup           - Полная установка и запуск проекта
echo   make.bat build           - Сборка Docker образов
echo   make.bat up              - Запуск контейнеров
echo   make.bat down            - Остановка контейнеров
echo   make.bat restart         - Перезапуск контейнеров
echo   make.bat logs            - Просмотр логов всех сервисов
echo   make.bat logs-backend    - Просмотр логов бэкенда
echo   make.bat logs-frontend   - Просмотр логов фронтенда
echo   make.bat logs-db         - Просмотр логов базы данных
echo   make.bat clean           - Очистка всех данных
echo   make.bat shell-backend   - Войти в shell контейнера бэкенда
echo   make.bat shell-db        - Войти в PostgreSQL
echo   make.bat migrate         - Применить миграции
echo   make.bat makemigrations  - Создать миграции
echo   make.bat createsuperuser - Создать суперпользователя
echo   make.bat collectstatic   - Собрать статические файлы
goto end

:end
