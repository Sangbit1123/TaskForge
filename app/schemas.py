from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role:str

class UserLogin(BaseModel):
    email: str
    password: str

class ProjectCreate(BaseModel):
    name: str
    description: str

class TaskCreate(BaseModel):
    
    title: str
    description: str
    assigned_to: int
    project_id: int
    priority: str
    due_date: date

class TaskStatusUpdate(BaseModel):
    status: str