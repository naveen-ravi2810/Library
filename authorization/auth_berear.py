from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth_handler import decodeJWT


class JWTBearer(HTTPBearer):
    role = "all"

    def __init__(self, auto_error: bool = True, role: str | None = "all"):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            try:
                payload = self.verify_jwt(credentials.credentials)
                if payload:
                    if self.role == "all":
                        return payload
                    elif self.role == "admin":
                        if payload["role"] == "admin":
                            return payload
                        raise HTTPException(
                            status_code=403, detail="Accessed only by Admins"
                        )
                    elif self.role == "reader":
                        if payload["role"] == "reader":
                            return payload
                        raise HTTPException(
                            status_code=403, detail="Accessed only by Readers"
                        )
                else:
                    raise HTTPException(
                        status_code=403, detail="Invalid or Expire Token"
                    )
            except HTTPException as e:
                raise HTTPException(status_code=403, detail=e.detail)
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> any:
        try:
            payload = decodeJWT(jwtoken)
        except Exception:
            payload = None
        if payload:
            return payload
        return False


common_auth = JWTBearer()
admin_auth = JWTBearer(role="admin")
reader_auth = JWTBearer(role="reader")
