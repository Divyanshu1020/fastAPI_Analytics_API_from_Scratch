from fastapi import APIRouter, Depends
from requests import Session

from api.event.models import EventCreateSchema, EventModel
from db.session import get_session


router = APIRouter()


@router.get("/")
def get_events():
    return {"message": "Hello API World"}

@router.post("/", response_model=EventModel)
def create_event(
        payload: EventCreateSchema,
        session: Session = Depends(get_session),
    ):
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
    

# @router.get("/")
# def get_events() -> EventListSchema:
#     return EventListSchema(events=[EventSchema(id=1), EventSchema(id=2)])
