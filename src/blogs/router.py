# Python imports

# Libraries imports
from robyn import SubRouter, Request

# Project imports
from src.blogs.service import BlogService
from src.blogs.schemas import BlogsResponse, BlogResponse
from config.config import settings
from config.database import get_connection

router = SubRouter(__name__, prefix=f"{settings.api_prefix}/blogs")

@router.get("/")
def get_all(request: Request) -> BlogsResponse:
    with get_connection() as db:
        service = BlogService(db)
        blogs = service.get_all()
    
    return BlogsResponse(status="success", status_code=200, data=blogs)
