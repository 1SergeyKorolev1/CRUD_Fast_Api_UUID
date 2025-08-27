from fastapi import FastAPI, Depends, HTTPException
from services import services
from models import models
from schemas import schemas
from db import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/tasks/", response_model=list[schemas.Task])
def get_all_tasks(db: Session = Depends(get_db)):
    return services.get_tasks(db)

@app.post("/tasks/", response_model=schemas.Task)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return services.create_task(db, task)