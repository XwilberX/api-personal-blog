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


class User(Body):
    pk: str
    created_at: str
    updated_at: str
    first_name: str
    middle_name: str
    last_name: str
    username: str
    email: str
    is_admin: bool
    picture_profile: str


class UserToken(Body):
    user: User
    token: str


class LoginUserResponse(JSONResponse):
    status: str
    status_code: int
    data: UserToken


class RegisterUserResponse(JSONResponse):
    status: str
    status_code: int
    data: dict
