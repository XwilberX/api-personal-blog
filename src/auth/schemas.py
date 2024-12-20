from robyn.types import Body, JSONResponse


class RegisterUser(Body):
    username: str
    email: str
    password: str
    is_admin: bool = False


class RegisterUserResponse(JSONResponse):
    status: str
    status_code: int
    data: dict
