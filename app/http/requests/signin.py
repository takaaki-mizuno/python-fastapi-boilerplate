from pydantic import BaseModel


class SignIn(BaseModel):
    email: str
    password: str
