from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_token(token)

    return payload

def admin_only(
    current_user = Depends(get_current_user)
):

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return current_user

@router.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    hashed_pw = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_pw,
        role=user.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if not verify_password(
        form_data.password,
        existing_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        data={
            "user_id": existing_user.id,
            "role": existing_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": existing_user.role
    }

@router.get("/profile")
def profile(
    current_user = Depends(get_current_user)
):

    return current_user