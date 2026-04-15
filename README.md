# Lucy - Multi-tenant API Gateway

Lucy is a multi-tenant API gateway that abstracts multiple messaging platforms (Telegram, Viber, Facebook Messenger) into a unified RESTful API.

## Features (still WIP)

- Multi-tenant architecture with OAuth2 authentication
- Unified API for multiple messaging platforms
- Asynchronous message processing with Celery
- Webhook subscriptions for real-time event delivery
- Comprehensive API documentation with OpenAPI/Swagger
- Production-ready Docker setup
- Structured logging with structlog
- Full test coverage support

## Technology Stack

- **Framework**: Django 5.0 + Django REST Framework
- **Database**: PostgreSQL 15
- **Cache/Queue**: Redis 7
- **Task Queue**: Celery with Redis broker
- **Authentication**: JWT (users) + OAuth2 (applications)
- **API Documentation**: drf-spectacular (OpenAPI 3.0)
- **Package Management**: uv

## Project Structure

```
lucy/
├── config/                 # Django project settings
│   ├── settings/
│   │   ├── base.py        # Base settings
│   │   ├── development.py # Dev settings
│   │   └── production.py  # Prod settings
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py          # Celery configuration
├── apps/
│   ├── users/             # User authentication
│   ├── applications/      # API client apps
│   ├── messages/          # Message handling
│   ├── platforms/         # Platform adapters
│   ├── webhooks/          # Webhook handling
│   ├── api/               # Shared API utilities
│   └── core/              # Shared utilities
├── manage.py
├── pyproject.toml         # Dependencies (uv)
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd lucy
```

2. Copy the environment file:
```bash
cp .env.example .env
```

3. Update the `.env` file with your settings (especially `SECRET_KEY` for production)

4. Build and start the services:
```bash
docker-compose up --build
```

5. The API will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/api/docs/
- Admin Panel: http://localhost:8000/admin/
- Health Check: http://localhost:8000/health/

### Initial Setup

Create a superuser to access the admin panel:
```bash
docker-compose exec api python manage.py createsuperuser
```

## Development

### Local Development Setup

1. Install uv (if not using Docker):
```bash
pip install uv
```

2. Install dependencies:
```bash
uv pip install -e ".[dev]"
```

3. Set up pre-commit hooks:
```bash
pre-commit install
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

### Running Tests

```bash
# Run all tests
docker-compose exec api pytest

# Run with coverage
docker-compose exec api pytest --cov

# Run specific test file
docker-compose exec api pytest apps/users/tests/test_models.py
```

### Code Quality

The project uses several tools for code quality:

- **black**: Code formatting
- **isort**: Import sorting
- **ruff**: Linting
- **mypy**: Type checking

Run all checks:
```bash
docker-compose exec api black .
docker-compose exec api isort .
docker-compose exec api ruff check .
docker-compose exec api mypy .
```

Or use pre-commit:
```bash
pre-commit run --all-files
```

### Database Migrations

```bash
# Create new migrations
docker-compose exec api python manage.py makemigrations

# Apply migrations
docker-compose exec api python manage.py migrate

# Show migration status
docker-compose exec api python manage.py showmigrations
```

### Celery Tasks

View Celery workers:
```bash
docker-compose logs -f celery_worker
docker-compose logs -f celery_beat
```

## API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/docs/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

## Environment Variables

Key environment variables (see `.env.example` for full list):

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `True` |
| `SECRET_KEY` | Django secret key | - |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://lucy:lucy@postgres:5432/lucy` |
| `REDIS_URL` | Redis connection string | `redis://redis:6379/0` |
| `JWT_ACCESS_TOKEN_LIFETIME_HOURS` | JWT access token lifetime | `1` |
| `JWT_REFRESH_TOKEN_LIFETIME_DAYS` | JWT refresh token lifetime | `7` |

## Docker Services

The `docker-compose.yml` defines the following services:

- **api**: Django application (port 8000)
- **postgres**: PostgreSQL database (port 5432)
- **redis**: Redis cache/broker (port 6379)
- **celery_worker**: Celery worker for async tasks
- **celery_beat**: Celery beat scheduler

## OAuth2 Scopes

Lucy supports the following OAuth2 scopes for application authentication:

- `messages:send` - Send messages through the platform
- `messages:read` - Read message history and status
- `messages:*` - Full access to messages
- `apps:manage` - Manage application settings
- `webhooks:manage` - Manage webhook subscriptions

## Architecture

Lucy follows a multi-layered architecture:

1. **API Layer**: RESTful endpoints with DRF
2. **Business Logic Layer**: Service classes and managers
3. **Data Access Layer**: Django ORM models
4. **Integration Layer**: Platform adapters (Telegram, Viber, Facebook)
5. **Async Processing Layer**: Celery tasks for background jobs

## Security

Lucy implements several security best practices:

- JWT-based authentication for users
- OAuth2 for application-to-API communication
- Input validation and sanitization
- SQL injection prevention (parameterized queries)
- CORS configuration
- HTTPS enforcement in production
- Security headers (HSTS, XSS protection, etc.)
- Password validation
- Rate limiting (to be implemented)

