# Task Manager

A simple task and project management web application built with FastAPI, PostgreSQL, SQLAlchemy, and Jinja2 templates.

## Overview

`Task Manager` provides a lightweight admin/member interface to manage projects, assign tasks, track status, and view dashboard metrics.

### Key Features

- User signup and login with JWT authentication
- Role-based access control for `admin` and `member`
- Project creation and deletion (admin only)
- Task creation, assignment, status updates, and deletion
- Dashboard statistics for total, completed, pending, and overdue tasks
- Server-rendered pages with a Bootstrap-powered UI

## Project Structure

- `app/main.py` - FastAPI application and router configuration
- `app/auth.py` - authentication helpers, JWT creation/verification, password hashing
- `app/database.py` - SQLAlchemy database connection and session setup
- `app/models.py` - ORM models for users, projects, and tasks
- `app/schemas.py` - Pydantic schemas for request validation
- `app/routes/` - API and frontend route definitions
- `app/templates/` - Jinja2 HTML templates for pages

## Requirements

The project dependencies are listed in `requirements.txt`.

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies.

```powershell
python -m pip install -r requirements.txt
```

4. Configure PostgreSQL.

Update the database URL in `app/database.py` if needed:

```python
DATABASE_URL = "postgresql://postgres:postgre123@localhost/task_manager"
```

5. Create the PostgreSQL database manually if it does not exist.

6. Run the application.

```powershell
python -m uvicorn app.main:app --reload
```

7. Open the browser:

```
http://127.0.0.1:8000/login-page
```

## Usage

The app includes the following frontend routes:

- `/login-page` - login screen
- `/dashboard-page` - dashboard overview
- `/projects-page` - project management
- `/tasks-page` - task management
- `/users-page` - team member listing

API routes are available for programmatic access.

## Notes

- Authentication is handled with JWT tokens stored in browser `localStorage`.
- `admin` users can create projects and tasks, delete them, and access all tasks.
- `member` users can view assigned tasks and update task status.
- Database tables are created automatically on startup via SQLAlchemy metadata.

## Recommended Improvements

- Add user registration restrictions and role validation.
- Improve error handling and authentication flow.
- Add a task member dropdown population function in `app/templates/task.html`.
- Add dedicated tests and database migration support.

## License

This repository is ready to use and extend for personal or team task management projects.
