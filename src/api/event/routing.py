from tkinter import E
from fastapi import APIRouter

from .models import EventListSchema, EventModel, EventSchema


router = APIRouter()


@router.get("/")
def get_events() -> EventListSchema:
    return EventListSchema(events=[EventSchema(id=1), EventSchema(id=2)])

@router.get("/{event_id}") 
def get_event(event_id: int) -> EventModel:
    return EventSchema(id=event_id)

@router.post("/")
def get_events(data):
    return