from robyn import Robyn

# config
from config.config import settings

# apps
from src.auth.views import router as auth_router

app = Robyn(__file__)


@app.get("/")
async def h(request):
    return "Hello, world"


app.include_router(router=auth_router)


app.start(port=settings.APP_PORT, host=settings.APP_HOST)
