from ..models import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    model = User

    def get_by_email(self, email: str) -> model:
        return self._db.query(self.model).filter(User.email == email).first()
