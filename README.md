# Healthcare Backend API

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.15-red?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-black?logo=jsonwebtokens&logoColor=white)

A RESTful backend for a healthcare application — manage patients, doctors, and their assignments with JWT-secured endpoints, built with Django REST Framework and PostgreSQL.

---

## Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Reference](#api-reference)

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | Django 4.2 + Django REST Framework 3.15 |
| Database | PostgreSQL 15 |
| Authentication | JWT — `djangorestframework-simplejwt` |
| Configuration | `python-decouple` |

---

## Project Structure

```
health_care/
├── authentication/       # Custom user model, register & login
├── patients/             # Patient CRUD APIs (user-scoped)
├── doctors/              # Doctor CRUD APIs
├── mappings/             # Patient-Doctor assignment APIs
├── healthcare_backend/   # Project settings & root URLs
├── manage.py
├── requirements.txt
└── .env.example
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL 15+

### Installation

```bash
git clone https://github.com/nikhilkumarpanigrahi/Health__care.git
cd Health__care

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

### Environment Setup

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### Database & Server

```bash
# Create the database in PostgreSQL
CREATE DATABASE healthcare_db;

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Server runs at `http://127.0.0.1:8000`

---

## API Reference

> All protected endpoints require the header:
> `Authorization: Bearer <access_token>`

---

### Authentication

#### `POST /api/auth/register/`
Register a new user.

**Request**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secret123"
}
```

**Response** `201 Created`
```json
{
  "message": "User registered successfully",
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

---

#### `POST /api/auth/login/`
Login and receive JWT tokens.

**Request**
```json
{
  "email": "john@example.com",
  "password": "secret123"
}
```

**Response** `200 OK`
```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

---

### Patients

> Patients are scoped to the authenticated user — each user only sees their own patients.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients/` | Add a new patient |
| GET | `/api/patients/` | List all patients |
| GET | `/api/patients/<id>/` | Get patient details |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

**Patient Object**
```json
{
  "name": "Jane Doe",
  "age": 28,
  "gender": "Female",
  "contact": "9876543210",
  "address": "123 Main St",
  "medical_history": "Hypertension"
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "name": "Jane Doe",
  "age": 28,
  "gender": "Female",
  "contact": "9876543210",
  "address": "123 Main St",
  "medical_history": "Hypertension",
  "created_by": 1,
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

---

### Doctors

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/doctors/` | Add a new doctor |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/<id>/` | Get doctor details |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

**Doctor Object**
```json
{
  "name": "Dr. Smith",
  "specialization": "Cardiology",
  "contact": "9876500000",
  "email": "smith@hospital.com",
  "experience_years": 10
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "name": "Dr. Smith",
  "specialization": "Cardiology",
  "contact": "9876500000",
  "email": "smith@hospital.com",
  "experience_years": 10,
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

---

### Patient-Doctor Mappings

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | List all mappings |
| GET | `/api/mappings/<patient_id>/` | Get all doctors for a patient |
| DELETE | `/api/mappings/<id>/` | Remove a doctor from a patient |

**Assign Request**
```json
{
  "patient": 1,
  "doctor": 1
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "patient": 1,
  "doctor": 1,
  "assigned_at": "2024-01-01T10:00:00Z"
}
```

**Get doctors for a patient** `GET /api/mappings/1/`
```json
[
  {
    "id": 1,
    "patient": 1,
    "doctor": {
      "id": 1,
      "name": "Dr. Smith",
      "specialization": "Cardiology",
      "contact": "9876500000",
      "email": "smith@hospital.com",
      "experience_years": 10
    },
    "assigned_at": "2024-01-01T10:00:00Z"
  }
]
```
