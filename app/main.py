from fastapi import FastAPI, Depends,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base

from app.routes.auth_routes import router as auth_router
from app.routes.project_routes import router as project_router
from app.routes.task_routes import router as task_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.user_routes import router as user_router
from app.routes.frontend_routes import router as frontend_router


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
app = FastAPI()
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(task_router)
app.include_router(dashboard_router)
app.include_router(user_router)
app.include_router(frontend_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():

    return RedirectResponse(
        url="/login-page"
    )
