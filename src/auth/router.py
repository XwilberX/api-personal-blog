from robyn import SubRouter, Request
import orjson

from config.config import settings

from config.database import get_connection
from src.auth.service import create_user
from src.auth.schemas import RegisterUser, RegisterUserResponse

router = SubRouter(__name__, prefix=f"{settings.api_prefix}/auth")
session = get_connection()


@router.post("/register")
async def register(request: Request, body: RegisterUser) -> RegisterUserResponse:
    with session as db:
        body = orjson.loads(request.body)
        result = create_user(db, body)

    if result is None:
        raise Exception("User not created")

    return RegisterUserResponse(status="success", status_code=200, data=result)
