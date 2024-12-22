# Python imports
import uuid

# Libraries imports
from robyn.types import Body, JSONResponse


class Blog(Body):
    pk: str = uuid.UUID
    created_at: str
    updated_at: str
    title: str
    description: str
    content: str


class BlogCreate(Body):
    title: str
    description: str
    content: str


class BlogUpdate(Body):
    title: str
    description: str
    content: str


class BlogResponse(JSONResponse):
    status: str
    status_code: int
    data: Blog


class BlogsResponse(JSONResponse):
    status: str
    status_code: int
    data: list[Blog]
