# Python imports
import uuid
from datetime import datetime

# Libraries imports
from pydantic import BaseModel
from robyn.types import JSONResponse


class Blog(BaseModel):
    pk: uuid.UUID
    created_at: datetime
    updated_at: datetime
    title: str
    description: str
    content: str


class BlogCreate(Blog):
    pass


class BlogResponse(JSONResponse):
    status: str
    status_code: int
    data: Blog


class BlogsResponse(JSONResponse):
    status: str
    status_code: int
    data: list[Blog]