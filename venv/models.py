from pydantic import BaseModel

class Task(BaseModel):
    id
    title: str
    descrption: str
    completed: bool=False