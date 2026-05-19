from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Task
from datetime import date

from app.routes.auth_routes import (
    get_current_user,
    admin_only
)


router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    total_tasks = db.query(Task).count()

    completed_tasks = db.query(Task).filter(
        Task.status == "Completed"
    ).count()

    pending_tasks = db.query(Task).filter(
        Task.status == "Pending"
    ).count()

    overdue_tasks = db.query(Task).filter(
        Task.due_date < date.today(),
        Task.status != "Completed"
    ).count()

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "overdue_tasks": overdue_tasks
    }