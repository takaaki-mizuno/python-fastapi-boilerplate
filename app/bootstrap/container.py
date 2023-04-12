from injector import Binder, Injector, InstanceProvider, singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from ..config import Config, config
from ..libraries import Hash
from ..repositories import UserRepository
from ..services import UserService


def build_container() -> None:
    injector = Injector([configure])
    injector.get(Config)


def configure(binder: Binder):
    injector = Injector()

    binder.bind(Config, to=config, scope=singleton)

    engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
    session_factory = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)
    db = scoped_session(session_factory)
    binder.bind(scoped_session, db)

    # Libraries
    _hash = Hash()
    binder.bind(Hash, to=_hash)

    # Repositories
    user_repository = UserRepository(db=db)
    binder.bind(UserRepository, to=user_repository)

    # Services
    user_service = UserService(user_repository=user_repository, _hash=_hash)
    binder.bind(UserService, to=user_service)
