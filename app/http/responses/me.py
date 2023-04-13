from pydantic import BaseModel

from app.models import User


class Me(BaseModel):
    id: str
    name: str
    email: str

    @classmethod
    def from_model(cls, model: User) -> 'Me':
        return cls(id=str(model.id), name=model.name, email=model.email)
