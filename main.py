# Python imports

# Libraries imports
from robyn import Robyn
from robyn.exceptions import HTTPException

# Project imports
from src.auth.router import router as auth_router
from src.blogs.router import router as blogs_router
from config.config import settings


app = Robyn(__file__)


@app.exception
def handle_exception(error):
    return {
        "status": "error",
        "status_code": error.status_code,
        "detail": error.detail,
    }


@app.get("/")
async def h(request):
    raise HTTPException(status_code=500, detail="Internal server error")


app.include_router(router=auth_router)
app.include_router(router=blogs_router)


app.start(port=settings.APP_PORT, host=settings.APP_HOST)
