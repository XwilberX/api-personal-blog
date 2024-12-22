# Python imports
from pwdlib import PasswordHash

# Libraries imports

# Project imports

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return password_hash.verify(password, hash)
