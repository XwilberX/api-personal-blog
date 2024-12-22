# Python imports

# Libraries imports
from robyn.authentication import AuthenticationHandler, BearerGetter
from robyn.robyn import Identity

# Project imports
from src.core.jwt import decode_access_token
from src.auth.repository import AuthUserRepository
from config.database import get_connection


class AuthMiddleware(AuthenticationHandler):
    def authenticate(self, request):
        token = self.token_getter.get_token(request)

        try:
            payload = decode_access_token(token)
            id = payload["id"]
            print(f"ID: {id}")
            # name = payload["name"]

        except Exception:
            return False
        
        with get_connection() as db:
            repository = AuthUserRepository(db)
            user = repository.get(id)

        return Identity(claims = {"user": user.as_dict_full})