# Python imports

# Libraries imports
from robyn import Robyn
from robyn.exceptions import HTTPException

# Project imports
from src.auth.router import router as auth_router
from src.auth.router import router_user as auth_router_user
from src.blogs.router import router as blogs_router


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
app.include_router(router=auth_router_user)


if __name__ == "__main__":
    app.start(port=8080, host="0.0.0.0")
