from uuid import UUID

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str
    status: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    uuid: UUID

    class Config:
        from_attribute = True
