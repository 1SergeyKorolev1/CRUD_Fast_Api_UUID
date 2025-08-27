from models.models import Task
from sqlalchemy.orm import Session
from schemas.schemas import TaskCreate
from fastapi import HTTPException
import psycopg2

def create_task(db: Session, data: TaskCreate):
    try:
        task = Task(**data.model_dump())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании задачи {str(e)}") from e

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_uuid:str):
    return db.query(Task).filter(Task.uuid==task_uuid).first()


