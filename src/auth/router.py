from robyn import SubRouter, Request
import orjson

from config.config import settings

from config.database import get_connection
from src.auth.service import AuthUserService
from src.auth.schemas import (
    LoginUser,
    RegisterUser,
    LoginUserResponse,
    RegisterUserResponse,
)

router = SubRouter(__name__, prefix=f"{settings.api_prefix}/auth")


@router.post("/login", openapi_name="Login user", openapi_tags=["Auth"])
def login(request: Request, body: LoginUser) -> LoginUserResponse:
    with get_connection() as db:
        body = orjson.loads(request.body)
        service = AuthUserService(db)
        status, user, token = service.login(body)

    if not status:
        return LoginUserResponse(status="Unauthorized", status_code=401, data={})

    return LoginUserResponse(
        status="Success",
        status_code=200,
        data={"user": user.as_dict_full, "token": token},
    )


@router.post("/register", openapi_name="Register user", openapi_tags=["Auth"])
def register(request: Request, body: RegisterUser) -> RegisterUserResponse:
    with get_connection() as db:
        body = orjson.loads(request.body)
        service = AuthUserService(db)
        user = service.add(body)

    return RegisterUserResponse(
        status="Success", status_code=200, data={"user": user.as_dict}
    )
