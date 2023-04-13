from pydantic import BaseModel


class AccessToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = 3600
    refresh_token: str = ""
