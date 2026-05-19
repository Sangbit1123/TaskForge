from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Project, Task

from app.routes.auth_routes import (
    get_current_user,
    admin_only
)
from app.schemas import ProjectCreate


router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.get("/projects")
def get_projects(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    projects = db.query(Project).all()

    return projects
@router.post("/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_only)
):

    new_project = Project(
        name=project.name,
        description=project.description,
        created_by=current_user["user_id"]
    )

    db.add(new_project)

    db.commit()

    db.refresh(new_project)

    return {
        "message": "Project created successfully",
        "project": new_project.name
    }
@router.delete("/projects/{project_id}")
def delete_project(project_id:int, db:Session=Depends(get_db),
                   current_user=Depends(admin_only)):
    project=db.query(Project).filter(Project.id==project_id).first()
    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )
    existing_tasks=db.query(Task).filter(Task.project_id==project_id).first()
    if existing_tasks:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete project with existing tasks"
        )
    db.delete(project)
    db.commit()
    return {
        "message":"Project deleted successfully"}
