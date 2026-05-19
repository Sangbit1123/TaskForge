from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User

from app.routes.auth_routes import (
    admin_only,
    get_current_user
)

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    users = db.query(User).all()

    return users
@router.get("/members")
def get_members(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    members = db.query(User).filter(
        User.role == "member"
    ).all()

    return members