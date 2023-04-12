from sqlalchemy import TIMESTAMP, BigInteger, Column, Integer, String
from sqlalchemy.sql import func, text

from .base import Base
from .types import UUID


class User(Base):
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
