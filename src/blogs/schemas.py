# Python imports
import uuid
from typing import List

# Libraries imports
from robyn.types import Body, JSONResponse


class Author(Body):
    pk: str


class FullAuthor(Body):
    pk: str
    username: str
    email: str
    name: str


class Blog(Body):
    pk: str = uuid.UUID
    created_at: str
    updated_at: str
    title: str
    description: str
    content: str
    author: Author


class BlogFullAuthor(Body):
    pk: str = uuid.UUID
    created_at: str
    updated_at: str
    title: str
    description: str
    content: str
    Author: FullAuthor


class BlogCreate(Body):
    title: str
    description: str
    content: str
    author: Author


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


class BlogCreateFullAuthorResponse(JSONResponse):
    status: str
    status_code: int
    data: BlogFullAuthor


class BlogsFullAuthorResponse(JSONResponse):
    status: str
    status_code: int
    data: list[BlogFullAuthor]
