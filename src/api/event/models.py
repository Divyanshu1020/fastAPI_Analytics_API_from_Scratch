from ast import Str
from typing import List, Optional
from sqlmodel import SQLModel, Field

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    page: Optional[int] = ''
    title: Optional[str] = ''
    description: Optional[str] = ''
    start: Optional[str] = ''
    end: Optional[str] = ''
    location: Optional[str] = ''
    
class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")

class EventUpdateSchema(SQLModel):
    description: Str

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int