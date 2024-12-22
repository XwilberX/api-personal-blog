# Python imports

# Libraries imports
from robyn.authentication import AuthenticationHandler
from robyn.robyn import Identity

# Project imports
from src.core.jwt import decode_access_token
from src.auth.service import AuthUserService
from config.database import get_connection


class AuthMiddleware(AuthenticationHandler):
    def authenticate(self, request):
        token = self.token_getter.get_token(request)

        try:
            payload = decode_access_token(token)
            id = payload["id"]

        except Exception:
            return False

        with get_connection() as db:
            service = AuthUserService(db)
            user = service.get(id)

        return Identity(claims={"user": user.as_dict_full_str})
