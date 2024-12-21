# Python imports

# Libraries imports
from robyn import SubRouter, Request, status_codes
import orjson

# Project imports
from src.blogs.service import BlogService
from src.blogs.schemas import BlogsResponse, BlogResponse, BlogCreate, BlogUpdate
from config.config import settings
from config.database import get_connection

router = SubRouter(__name__, prefix=f"{settings.api_prefix}/blogs")


@router.get("/", openapi_name="Get all blogs", openapi_tags=["Blogs"])
def get_all(request: Request) -> BlogsResponse:
    with get_connection() as db:
        service = BlogService(db)
        blogs = service.get_all()

    return BlogsResponse(
        status="success", status_code=status_codes.HTTP_200_OK, data=blogs
    )


@router.get("/:pk", openapi_name="Get blog by pk", openapi_tags=["Blogs"])
def get_by_pk(request: Request) -> BlogResponse:
    pk = request.path_params["pk"]
    with get_connection() as db:
        service = BlogService(db)
        blog = service.get(pk)

    return BlogResponse(
        status="success", status_code=status_codes.HTTP_200_OK, data=blog.as_dict_full
    )


@router.post("/create", openapi_name="Create blog", openapi_tags=["Blogs"])
def create(request: Request, body: BlogCreate) -> BlogResponse:
    with get_connection() as db:
        body = orjson.loads(request.body)
        service = BlogService(db)
        blog = service.add(body)

    return BlogResponse(
        status="success",
        status_code=status_codes.HTTP_201_CREATED,
        data=blog.as_dict_full,
    )


@router.put("/:pk", openapi_name="Update blog", openapi_tags=["Blogs"])
def update(request: Request, body: BlogUpdate) -> BlogResponse:
    pk = request.path_params["pk"]
    with get_connection() as db:
        body = orjson.loads(request.body)
        service = BlogService(db)
        blog = service.update(pk, body)

    return BlogResponse(
        status="success",
        status_code=status_codes.HTTP_200_OK,
        data=blog.as_dict_full,
    )


@router.delete("/:pk", openapi_name="Delete blog", openapi_tags=["Blogs"])
def delete(request: Request) -> None:
    pk = request.path_params["pk"]
    with get_connection() as db:
        service = BlogService(db)
        _ = service.delete(pk)

    return None
