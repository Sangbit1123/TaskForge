from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Task

from app.routes.auth_routes import (
    get_current_user,
    admin_only
)
from app.schemas import TaskCreate, TaskStatusUpdate

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.post("/tasks")
def create_task(task: TaskCreate,db: Session = Depends(get_db),current_user = Depends(admin_only)):
    new_task=Task(title=task.title,description=task.description,assigned_to=task.assigned_to,project_id=task.project_id,priority=task.priority,due_date=task.due_date   )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task created successfully", "task": new_task}
@router.get("/tasks")
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(admin_only)
):

    tasks = db.query(Task).all()

    return tasks
@router.get("/my-tasks")
def get_my_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    tasks = db.query(Task).filter(
        Task.assigned_to == current_user["user_id"]
    ).all()

    return tasks
@router.put("/tasks/{task_id}/status")
def update_task_status(
    task_id: int,
    task_update: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()
    allowed_status = [
    "Pending",
    "In Progress",
    "Completed"
]

    if task_update.status not in allowed_status:

        raise HTTPException(
        status_code=400,
        detail="Invalid status"
        )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if current_user["role"]!="admin" and task.assigned_to != current_user["user_id"]:

        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    task.status = task_update.status

    db.commit()

    db.refresh(task)

    return {
        "message": "Task status updated",
        "new_status": task.status
    }
@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_only)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)

    db.commit()

    return {
        "message": "Task deleted successfully"
    }