from models.models import Task
from sqlalchemy.orm import Session
from schemas.schemas import TaskCreate

def create_task(db: Session, data: TaskCreate):
    task = Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    return db.query(Task).all()

