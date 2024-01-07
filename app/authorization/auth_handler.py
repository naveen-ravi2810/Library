import time
from typing import Dict

import jwt
from core.settings import settings


JWT_SECRET = settings.JWT_SECRET_KEY
JWT_ALGORITHM = "HS256"


# function used for signing the JWT string
def signJWT(user) -> Dict[str, str]:
    payload = {
        "sub": user.user_id,
        "exp": time.time() + 600,
        "role": user.user_role,
        "iat": time.time(),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except Exception:
        return {}
