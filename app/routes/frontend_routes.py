from fastapi import APIRouter, Request

from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)

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
def tasks_page(request: Request):
    return templates.TemplateResponse(
        request,
        "task.html"
    )
@router.get("/users-page")
def users_page(request: Request):
    return templates.TemplateResponse(
        request,
        "users.html"
    )