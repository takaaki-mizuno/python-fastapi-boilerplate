from sqlalchemy import TIMESTAMP, BigInteger, Column, Integer, String, event
from sqlalchemy.sql import func, text
from starlette.authentication import BaseUser

from ..libraries import Hash
from .base import Base
from .types import UUID


class User(Base, BaseUser):
    __tablename__ = 'users'
    id = Column(UUID,
                primary_key=True,
                server_default=text('gen_random_uuid()'))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        onupdate=func.now(),
                        server_default=func.now())
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())

    @property
    def is_authenticated(self) -> bool:
        raise NotImplementedError()  # pragma: no cover

    @property
    def display_name(self) -> str:
        return self.name

    @property
    def identity(self) -> str:
        return str(self.id)
