from sqlalchemy import Column, Date, DateTime, Integer, String,ForeignKey
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String,unique=True, index=True)
    email=Column(String,unique=True, index=True)
    password=Column(String) 
    role=Column(String) 

class Project(Base):
    __tablename__="projects"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True, index=True)
    description=Column(String)
    created_by=Column(Integer,ForeignKey("users.id"))

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    description = Column(String)

    status = Column(String, default="Pending")
    priority = Column(String)

    due_date = Column(Date)

    created_at = Column(
    DateTime,
    default=datetime.utcnow)


    assigned_to = Column(
        Integer,
        ForeignKey("users.id")
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )
    