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
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register a new user | No |
| POST | `/api/auth/login/` | Login and receive JWT token | No |

### Patient Management
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/patients/` | Add a new patient | Yes |
| GET | `/api/patients/` | List all patients (by logged-in user) | Yes |
| GET | `/api/patients/<id>/` | Get patient details | Yes |
| PUT | `/api/patients/<id>/` | Update patient | Yes |
| DELETE | `/api/patients/<id>/` | Delete patient | Yes |

### Doctor Management
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/doctors/` | Add a new doctor | Yes |
| GET | `/api/doctors/` | List all doctors | Yes |
| GET | `/api/doctors/<id>/` | Get doctor details | Yes |
| PUT | `/api/doctors/<id>/` | Update doctor | Yes |
| DELETE | `/api/doctors/<id>/` | Delete doctor | Yes |

> More endpoints will be added as features are implemented.

### Authentication Usage

**Register:**
```json
POST /api/auth/register/
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secret123"
}
```

**Login:**
```json
POST /api/auth/login/
{
  "email": "john@example.com",
  "password": "secret123"
}
```

Response returns `access` and `refresh` JWT tokens. Pass the access token in subsequent requests:
```
Authorization: Bearer <access_token>
```

## Project Structure

```
health_care/
├── healthcare_backend/   # Django project settings & root URLs
├── authentication/       # Custom user model, register & login APIs
├── patients/             # Patient model and CRUD APIs
├── doctors/              # Doctor model and CRUD APIs
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```
