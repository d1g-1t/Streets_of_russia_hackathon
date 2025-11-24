# 🏆 ХАКАТОН "УЛИЦЫ РОССИИ"

> **Платформа для объединения уличной культуры России**  
> Паркур, стрит-арт, брейкданс, воркаут - всё в одном месте! 

[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Django](https://img.shields.io/badge/Django-5.0.6-green?logo=django)](https://www.djangoproject.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14.2.3-black?logo=next.js)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue?logo=postgresql)](https://www.postgresql.org/)

## 🚀 Быстрый старт

**Запуск проекта в одну команду:**

**Linux/macOS:**
```bash
git clone git@github.com:hakaton-streetsOfRussia/streets_backend.git
cd streets_backend
make setup
```

**Windows:**
```bash
git clone git@github.com:d1g-1t/Streets_of_russia_hackathon.git
cd streets_backend
make.bat setup
```

⏱️ **Первый запуск занимает 3-5 минут** (сборка Docker образов, загрузка зависимостей, применение миграций).  
Последующие запуски — 30 секунд.

**Готово!** Проект запущен. Доступные сервисы:
- 🎨 **Frontend** — http://localhost:3000
- ⚙️ **Backend API (Swagger)** — http://localhost:8000/swagger/
- 🔧 **Admin Panel** — http://localhost:8000/admin/

## 📋 Системные требования

**Минимальные требования:**
- 🐳 **Docker** версия 20.10 или выше - [скачать](https://www.docker.com/get-started)
- 🐙 **Docker Compose** версия 1.29 или выше - [установить](https://docs.docker.com/compose/install/)

**Платформы:**
- ✅ Linux / macOS - используйте `make`
- ✅ Windows - используйте `make.bat` (входит в комплект)

## 🛠️ Команды управления проектом

> **Для Windows:** используйте `make.bat` вместо `make` (например: `make.bat setup`)

### Основные команды

| Команда | Описание |
|---------|----------|
| `make setup` | 🚀 Полная установка и запуск проекта (первый запуск) |
| `make up` | ▶️ Запустить все сервисы |
| `make down` | ⏸️ Остановить все сервисы |
| `make restart` | 🔄 Перезапустить сервисы |
| `make build` | 🏗️ Пересобрать Docker образы |

### Мониторинг и отладка

| Команда | Описание |
|---------|----------|
| `make logs` | 📊 Просмотр логов всех сервисов |
| `make logs-backend` | 🔍 Просмотр логов backend |
| `make logs-frontend` | 🎨 Просмотр логов frontend |
| `make shell-backend` | 🐚 Консоль внутри backend контейнера |
| `make shell-db` | 🗄️ Консоль PostgreSQL |

### Работа с БД

| Команда | Описание |
|---------|----------|
| `make migrate` | 📝 Применить миграции |
| `make makemigrations` | 📝 Создать новые миграции |
| `make createsuperuser` | 👑 Создать суперпользователя |
| `make collectstatic` | 📦 Собрать статические файлы |

### Очистка

| Команда | Описание |
|---------|----------|
| `make clean` | 🧹 Удалить все контейнеры, образы и volumes |

## 📖 Инструкция по развертыванию

### Первый запуск проекта

**Шаг 1. Клонирование репозитория**
```bash
git clone git@github.com:d1g-1t/Streets_of_russia_hackathon.git
cd streets_backend
```

**Шаг 2. Автоматическая установка**
```bash
make setup  # Linux/macOS
make.bat setup  # Windows
```

Команда `make setup` — это **всё, что нужно**. Она автоматически:
- ✅ Создаёт `.env` из шаблона *(потому что мы не коммитим секреты в git, правда?)*
- ✅ Собирает Docker образы для backend и frontend *(займёт 3-5 минут при первом запуске)*
- ✅ Запускает все сервисы с правильными зависимостями *(PostgreSQL → Django → Next.js)*
- ✅ Ждёт инициализации PostgreSQL *(health checks творят чудеса)*
- ✅ Применяет миграции БД *(Django ORM в действии)*
- ✅ Собирает статику *(collectstatic, старый добрый друг)*

⏱️ **Время выполнения:** 3-5 минут при первом запуске, 30 секунд при повторных.

**Шаг 3. Создание администратора (опционально)**
```bash
make createsuperuser
```
Введите учётные данные и получите доступ к Django Admin — той самой админке, которой все завидуют.

### Ежедневное использование

**Запуск проекта:**
```bash
make up
```

**Остановка проекта:**
```bash
make down
```
> Не забываем graceful shutdown — контейнеры умеют корректно завершать работу.

**Просмотр логов:**
```bash
make logs  # Все сервисы сразу
make logs-backend  # Только Django (когда что-то пошло не так)
make logs-frontend  # Только Next.js (когда компонент рендерится не туда)
```

**Перезапуск после изменений:**
```bash
make restart
```

### Работа с базой данных

**Применение миграций:**
```bash
make migrate
```
> Django ORM делает миграции безболезненными. Почти всегда.

**Создание новых миграций:**
```bash
make makemigrations
```

**Доступ к PostgreSQL консоли:**
```bash
make shell-db
```
> Прямой доступ к psql для тех случаев, когда нужен сырой SQL.

### Разработка

**Доступ к backend контейнеру:**
```bash
make shell-backend
```
> Полезно для отладки, запуска Django shell или проверки установленных пакетов.

**Сбор статических файлов:**
```bash
make collectstatic
```

## 🏗️ Архитектура проекта

### Компоненты системы

Проект построен на классической трёхзвенной архитектуре:

1. **PostgreSQL** (порт 5432) — Реляционная база данных  
   *Потому что NoSQL не всегда ответ, и ACID транзакции это круто*

2. **Django Backend** (порт 8000) — REST API сервер  
   *Django REST Framework + OpenAPI документация из коробки*

3. **Next.js Frontend** (порт 3000) — SSR React приложение  
   *Server-Side Rendering для SEO и производительности*

Все компоненты работают в изолированных Docker контейнерах с настроенными health checks и auto-restart политиками.

### Структура проекта

```
streets_of_russia_backend/
├── backend/              # Django REST API
│   ├── aboutus/         # Модуль "О нас"
│   ├── blog/            # Блог
│   ├── contacts/        # Контакты
│   ├── events/          # События
│   ├── streetculture/   # Уличная культура
│   ├── users/           # Пользователи
│   └── streets_backend/ # Настройки проекта
├── frontend/            # Next.js приложение
│   ├── src/
│   │   ├── app/        # Страницы приложения
│   │   └── components/ # Компоненты
│   └── public/         # Статические файлы
├── infra/              # Конфигурация для production
├── docker-compose.yml  # Docker Compose для локальной разработки
├── Makefile           # Автоматизация команд
└── .env.example       # Пример переменных окружения
```

## ⚙️ Конфигурация

### Переменные окружения

Все настройки проекта централизованы в файле `.env`:

```env
# Django Configuration
SECRET_KEY=your-secret-key              # Криптографический ключ Django
DEBUG=True                              # True только для development!
ALLOWED_HOSTS=localhost,127.0.0.1       # CORS и безопасность

# PostgreSQL Configuration
POSTGRES_DB=streets_db                  # Название базы данных
POSTGRES_USER=postgres                  # Пользователь БД
POSTGRES_PASSWORD=postgres              # Пароль (измените для production!)
POSTGRES_HOST=db                        # Имя сервиса в Docker Compose
POSTGRES_PORT=5432                      # Стандартный порт PostgreSQL

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000  # Базовый URL для API запросов
```

> ⚠️ **Security Note:** В production обязательно измените `SECRET_KEY`, установите `DEBUG=False` и используйте сложный пароль для БД. Мы серьёзно.

## 👥 Команда проекта

**Проект-менеджмент:**
- [Екатерина Санникова](https://t.me/sannikovakat) — Project Manager
- [Марина Погиева](https://t.me/mpogieva) — Product Manager

**Design:**
- [Аля Ковач](https://t.me/AlyaKovach) — UI/UX Designer
- [Диана Сырлыбаева](https://t.me/DianaSyrlybaeva) — UI/UX Designer

**Frontend Development:**
- [Лев Смиронов](https://github.com/levsmirnov1999) — Next.js Developer
- [Даниил Андреев](https://github.com/accrrsd) — React Developer

**Backend Development:**
- [Павел Охрим](https://github.com/d1g-1t) — Django Developer
- [Алексей Орел](https://github.com/orel333) — Python Developer

## 🛠️ Технологический стек

### Backend Stack
- ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=Django) **Django 5.0.6** — Python web framework  
  *Потому что "batteries included" это не просто слова*
  
- ![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-092E20?style=flat-square&logo=Django) **DRF 3.15.1** — REST API toolkit  
  *Serializers, ViewSets, и автоматическая пагинация. Красота.*
  
- ![Gunicorn](https://img.shields.io/badge/-Gunicorn-000000?style=flat-square&logo=Gunicorn) **Gunicorn 20.1.0** — WSGI HTTP сервер  
  *Production-ready с worker процессами*
  
- ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=PostgreSQL) **PostgreSQL 13** — Реляционная БД  
  *ACID транзакции, JSON поддержка, и годы стабильности*
  
- **[Djoser](https://djoser.readthedocs.io/en/latest/)** — Authentication  
  *JWT/Token auth из коробки*
  
- **[DRF-YASG](https://drf-yasg.readthedocs.io/en/stable/)** — API Documentation  
  *OpenAPI 3.0 спецификация автоматически*
  
- **[Django-Filter](https://django-filter.readthedocs.io/en/stable/)** — QuerySet filtering  
  *Потому что SQL WHERE вручную писать в 2025 не надо*

### Frontend Stack
- ![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=Next.js) **Next.js 14.2.3** — React framework  
  *App Router, Server Components, и SSR для SEO*
  
- ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=React&logoColor=black) **React 18** — UI library  
  *Concurrent rendering и Suspense готовы к бою*
  
- ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=TypeScript&logoColor=white) **TypeScript 5** — Typed JavaScript  
  *Compile-time ошибки лучше, чем runtime. Всегда.*
  
- ![Tailwind CSS](https://img.shields.io/badge/-Tailwind%20CSS-38B2AC?style=flat-square&logo=Tailwind-CSS&logoColor=white) **Tailwind 3.4** — Utility-first CSS  
  *JIT компилятор и минимальный bundle размер*
  
- **[NextUI](https://nextui.org/)** + **[PrimeReact](https://primereact.org/)** — UI Components  
  *Готовые компоненты вместо велосипедов*
  
- **[Framer Motion](https://www.framer.com/motion/)** — Animations  
  *Плавные 60fps анимации с минимальным кодом*

### DevOps & Infrastructure
- ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=Docker&logoColor=white) **Docker** — Containerization  
  *"Works on my machine" → "Works everywhere"*
  
- ![Nginx](https://img.shields.io/badge/-Nginx-269539?style=flat-square&logo=Nginx&logoColor=white) **Nginx** — Reverse Proxy  
  *SSL termination, gzip, и статика с максимальной скоростью*
  
- **Docker Compose** — Container Orchestration  
  *Многоконтейнерные приложения одной командой*
  
- **Make** — Build Automation  
  *Потому что `make setup` лучше, чем 15 строк команд*

---

## 📦 Дополнительные библиотеки

- **[Pillow](https://pillow.readthedocs.io/en/stable/)** — Image processing library  
  *Ресайз, crop, и фильтры для загружаемых изображений*
  
- **[Python-Decouple](https://pypi.org/project/python-decouple/)** — Settings management  
  *Переменные окружения без головной боли*
  
- **[QRCode](https://pypi.org/project/qrcode/)** — QR code generator  
  *Генерация QR кодов для событий*

---
