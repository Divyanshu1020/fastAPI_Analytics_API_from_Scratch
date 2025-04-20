from re import L
from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.event import router as event_router
from db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix="/api/events", tags=["events"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello")
def health_check():
    return {"status": "ok"}