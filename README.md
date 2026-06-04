# Healthcare Backend API

A RESTful backend system for a healthcare application built with Django, Django REST Framework, and PostgreSQL.

## Tech Stack

- **Framework**: Django 4.2, Django REST Framework 3.15
- **Database**: PostgreSQL
- **Authentication**: JWT via `djangorestframework-simplejwt`
- **Config**: `python-decouple` for environment variables

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL 15+

### Setup

```bash
# Clone the repository
git clone https://github.com/nikhilkumarpanigrahi/Health_care.git
cd Health_care

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your database credentials and secret key
```

### Create PostgreSQL Database

```sql
CREATE DATABASE healthcare_db;
```

### Run Migrations

```bash
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and receive JWT token |

> More endpoints will be added as features are implemented.

## Project Structure

```
health_care/
├── healthcare_backend/   # Django project settings
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```
