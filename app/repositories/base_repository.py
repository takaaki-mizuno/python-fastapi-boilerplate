from injector import Injector, inject
from sqlalchemy.orm import scoped_session

from ..models.base import Base


class BaseRepository(object):
    model: Base = Base

    @inject
    def __init__(self, db: scoped_session):
        self._db = db

    def list(self, offset: int = 0, limit: int = 20) -> [model]:
        return self._db.query(self.model).limit(limit).offset(offset).all()

    def get(self, _id: str) -> model:
        return self._db.query(self.model).filter(self.model.id == _id).first()
