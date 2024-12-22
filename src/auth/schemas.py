from robyn.types import Body, JSONResponse


class RegisterUser(Body):
    first_name: str
    middle_name: str = None
    last_name: str
    username: str
    email: str
    password: str
    is_admin: bool = False
    picture_profile: str = None


class LoginUser(Body):
    email: str
    password: str


class LoginUserResponse(JSONResponse):
    status: str
    status_code: int
    data: dict


class RegisterUserResponse(JSONResponse):
    status: str
    status_code: int
    data: dict
