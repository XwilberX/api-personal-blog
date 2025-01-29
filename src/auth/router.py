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
    UsersResponse,
)

router = SubRouter(__name__, prefix=f"{settings.api_prefix}/auth")
router_user = SubRouter(__name__, prefix=f"{settings.api_prefix}/users")


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
    user = None

    with get_connection() as db:
        body = orjson.loads(request.body)
        service = AuthUserService(db)
        user = service.add(body)

    if not user:
        return RegisterUserResponse(
            status="Failed",
            status_code=400,
            data={"message": "Error, user not created"},
        )

    return RegisterUserResponse(
        status="Success", status_code=200, data={"user": user.as_dict_full}
    )


@router_user.get(
    "/", openapi_name="Get all users", openapi_tags=["Users"], auth_required=True
)
def get_all(request: Request) -> UsersResponse:
    print("Get all users")
    with get_connection() as db:
        service = AuthUserService(db)
        users = service.get_all()

    print(f"Users: {users}")

    return UsersResponse(status="success", status_code=200, data=users)
