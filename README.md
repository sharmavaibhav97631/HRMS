# HRMS Lite — A Lightweight HR Management System

A simple and efficient **Human Resources Management System (HRMS)** built with Django. Manage employees and track attendance with an intuitive web interface. Perfect for small organizations needing basic HR functionality without complexity.

---

## 📋 Quick Navigation

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Database Models](#-database-models)
- [Routes & URLs](#-routes--urls)
- [Django Commands](#-django-commands)
- [Troubleshooting](#-troubleshooting)

---

## ✨ Features

- ✅ **Employee Management** — Add, view, and manage employee records with auto-generated IDs
- ✅ **Attendance Tracking** — Mark attendance (Present/Absent) for each employee by date
- ✅ **Admin Dashboard** — Django admin interface with enhanced UI (Jazzmin)
- ✅ **Data Integrity** — Email validation, unique constraints, duplicate prevention
- ✅ **CORS Support** — Ready for frontend integration
- ✅ **REST Framework** — DRF serializers for API expansion
- ✅ **PostgreSQL Ready** — Includes psycopg2 for production databases

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | Django 6.0.2 |
| **API** | Django REST Framework 3.16.1 |
| **Database** | SQLite (dev), PostgreSQL-ready (prod) |
| **Admin UI** | Jazzmin 3.0.2 |
| **Middleware** | CORS, Sessions, Authentication |
| **Python** | 3.12+ |

**All Dependencies:** See [requirements.txt](requirements.txt)

---

## 📦 Prerequisites

Before starting, ensure you have:

- **Python 3.8 or higher** — Check with `python --version`
- **pip** — Package manager (comes with Python)
- **(Optional) PostgreSQL** — For production deployments

---

## 🚀 Getting Started

### Step 1: Navigate to Project
```bash
cd /home/vaibhav_sharma/Project/hrms-lite/hrms
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Admin User (Optional)
```bash
python manage.py createsuperuser
# Enter username, email, and password when prompted
```

### Step 6: Start Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Application

| Page | URL |
|------|-----|
| 🏠 Home | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| 👥 Employees List | [http://127.0.0.1:8000/employees/list/](http://127.0.0.1:8000/employees/list/) |
| ➕ Add Employee | [http://127.0.0.1:8000/employees/create/](http://127.0.0.1:8000/employees/create/) |
| 📋 Attendance | [http://127.0.0.1:8000/attendance/list/](http://127.0.0.1:8000/attendance/list/) |
| ⚙️ Admin Panel | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |

---

## 📂 Project Structure

```
hrms/
├── 📄 manage.py                      # Django CLI tool
├── 📄 requirements.txt               # Python dependencies
├── 📄 README.md                      # This file
├── 📄 Dockerfile                     # Docker configuration
├── 📄 docker-compose.yml             # Docker Compose setup
├── 📄 .env                           # Environment variables (not in repo)
│
├── 📁 hrms/                          # Main Django project config
│   ├── 📄 __init__.py
│   ├── 📄 settings.py                # App settings, database, installed apps
│   ├── 📄 urls.py                    # Main URL router
│   ├── 📄 views.py                   # Home view
│   ├── 📄 asgi.py                    # ASGI server entry point
│   ├── 📄 wsgi.py                    # WSGI server entry point
│   └── 📁 __pycache__/
│
├── 📁 employees/                     # Employee Management App
│   ├── 📄 models.py                  # Employee model
│   ├── 📄 views.py                   # List, create, delete employees
│   ├── 📄 urls.py                    # Employee URL patterns
│   ├── 📄 admin.py                   # Admin configuration
│   ├── 📄 serializers.py             # DRF serializers
│   ├── 📄 apps.py
│   ├── 📄 tests.py
│   │
│   ├── 📁 templates/employees/
│   │   ├── 📄 employee_list.html     # Display all employees
│   │   └── 📄 employee_form.html     # Add new employee form
│   │
│   ├── 📁 migrations/
│
├── 📁 attendance/                    # Attendance Tracking App
│   ├── 📄 models.py                  # Attendance model
│   ├── 📄 views.py                   # Mark & list attendance
│   ├── 📄 urls.py                    # Attendance URL patterns
│   ├── 📄 admin.py                   # Admin configuration
│   ├── 📄 serializers.py             # DRF serializers
│   ├── 📄 apps.py
│   ├── 📄 tests.py
│   │
│   ├── 📁 templates/attendance/
│   │   └── 📄 attendance_list.html   # Mark & view attendance
│   │
│   ├── 📁 migrations/
│
├── 📁 templates/                     # Shared templates
│   └── 📄 base.html                  # Base template for all pages
│
└── 📁 venv/                          # Virtual environment (not in repo)
```

---

## 🗄 Database Models

### Employee Model

**Fields:**
| Field | Type | Notes |
|-------|------|-------|
| `employee_id` | CharField | Auto-generated as `EMP0001`, `EMP0002`, etc. |
| `full_name` | CharField | Max 100 characters |
| `email` | EmailField | **Unique** — No two employees can have same email |
| `department` | CharField | Max 100 characters |

**Example:**
```python
Employee(
    employee_id="EMP0001",
    full_name="John Doe",
    email="john@example.com",
    department="Engineering"
)
```

---

### Attendance Model

**Fields:**
| Field | Type | Notes |
|-------|------|-------|
| `employee` | ForeignKey | Links to Employee (cascade delete) |
| `date` | DateField | Date of attendance |
| `status` | CharField | Either "Present" or "Absent" |

**Constraints:**
- **Unique Together** — Only one attendance record per employee per date
- **Ordering** — Latest dates appear first
- **Related Name** — `employee.attendance_records` to access all records

**Example:**
```python
Attendance(
    employee=john_employee,
    date="2026-02-10",
    status="Present"
)
```

---

## 🌐 Routes & URLs

### Employee Routes

| Method | Endpoint | Purpose | Handler |
|--------|----------|---------|---------|
| `GET` | `/employees/list/` | View all employees | `employee_list` |
| `GET` | `/employees/create/` | Show employee form | `employee_create` |
| `POST` | `/employees/create/` | Save new employee | `employee_create` |
| `POST` | `/employees/delete/<id>/` | Delete employee | `employee_delete` |

**Employee Form Fields:**
- `full_name` (required)
- `email` (required, must be unique)
- `department` (required)

---

### Attendance Routes

| Method | Endpoint | Purpose | Handler |
|--------|----------|---------|---------|
| `GET` | `/attendance/list/` | View all attendance records | `attendance_list` |
| `GET` | `/attendance/list/?employee=<id>` | Filter by employee | `attendance_list` |
| `POST` | `/attendance/list/` | Mark attendance | `mark_attendance` |

**Attendance Form Fields:**
- `employee` (required dropdown)
- `date` (required date picker)
- `status` (required: Present/Absent)

**Filter Example:**
```
GET /attendance/list/?employee=1
```
Shows only attendance records for employee with ID = 1

---

## 📝 Django Commands

### Running the Server

```bash
# Default (localhost:8000)
python manage.py runserver

# Custom port
python manage.py runserver 8001

# Accessible from other machines
python manage.py runserver 0.0.0.0:8000
```

### Database Migrations

```bash
# Apply all pending migrations
python manage.py migrate

# Create new migration after model changes
python manage.py makemigrations

# Show pending migrations
python manage.py showmigrations

# Revert to specific migration
python manage.py migrate employees 0001
```

### User & Permissions

```bash
# Create superuser (admin account)
python manage.py createsuperuser

# Change password
python manage.py changepassword username

# Create normal user
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('username', 'email@example.com', 'password')
```

### Testing

```bash
# Run all tests
python manage.py test

# Run app-specific tests
python manage.py test employees
python manage.py test attendance

# Run specific test
python manage.py test employees.tests.EmployeeTestCase

# Verbose output
python manage.py test -v 2
```

### Utilities

```bash
# Access Django shell (Python REPL with Django context)
python manage.py shell

# Collect static files
python manage.py collectstatic

# Show all available commands
python manage.py help
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'django'"

**Cause**: Dependencies not installed or virtual environment not activated

**Solution**:
```bash
source venv/bin/activate  # Activate venv
pip install -r requirements.txt
```

---

### "No such table: employees_employee"

**Cause**: Database migrations not applied

**Solution**:
```bash
python manage.py migrate
```

---

### "Email already exists" Error

**Cause**: Employee with same email already in database

**Solution**: 
- Check employee list and use a different email
- Or delete existing employee first

---

### Port 8000 Already in Use

**Cause**: Another process running on port 8000

**Solution**:
```bash
# Use different port
python manage.py runserver 8001

# Or find and kill the process
lsof -i :8000
kill -9 <PID>
```

---

### "CSRF token missing or incorrect"

**Cause**: Form doesn't include CSRF token (normal in development)

**Solution**: Ensure form has:
```html
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

---

## 📚 Next Steps

### To Extend This Project:

- 🔐 **Authentication** — Add login/logout for secure access
- 📧 **Email Notifications** — Send notifications for attendance
- 💰 **Payroll Module** — Add salary and payment tracking
- 🏖️ **Leave Management** — Track employee leave/absences
- 📱 **REST API** — Create full REST API endpoints
- 📊 **Reports** — Generate attendance and payroll reports
- 🐳 **Docker** — Deploy using Docker containers

---

## 📄 License

This project is **open source** and free to use or modify.

---

## ❓ Need Help?

- 📖 Check this README
- 🔍 Review [Django Documentation](https://docs.djangoproject.com/)
- 💬 Run `python manage.py help` for command info
- 🐛 Check console output for error messages

---

**Happy coding! 🚀**
