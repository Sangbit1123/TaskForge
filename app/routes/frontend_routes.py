from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User, Project, Task

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/login-page")
def login_page(request: Request):

    return templates.TemplateResponse(
        request,
        "login.html"
    )

@router.get("/dashboard-page")
def dashboard_page(request: Request):

    return templates.TemplateResponse(
        request,
        "dashboard.html"
    )

@router.get("/projects-page")
def projects_page(request: Request):

    return templates.TemplateResponse(
        request,
        "project.html"
    )

@router.get("/tasks-page")
def tasks_page(request: Request, db: Session = Depends(get_db)):

    users = db.query(User).all()

    projects = db.query(Project).all()

    tasks = db.query(Task).all()

    return templates.TemplateResponse(
        request,
        "task.html",
        {
            "users": users,
            "projects": projects,
            "tasks": tasks
        }
    )

@router.get("/users-page")
def users_page(request: Request):

    return templates.TemplateResponse(
        request,
        "users.html"
    )