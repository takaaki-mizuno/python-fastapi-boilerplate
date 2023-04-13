from app.bootstrap.container import build_container
from sqlalchemy.orm import scoped_session

from app.libraries import Hash
from app.models import Base
from injector import Binder, Injector, InstanceProvider, singleton


class BaseSeeder:
    model = Base

    def get_data(self) -> list:
        raise NotImplementedError

    def __init__(self, injector: Injector = None):
        self.db = injector.get(scoped_session)
        self.hash = injector.get(Hash)

    def run(self):
        for data in self.get_data():
            seed = self.model(**data)
            self.db.add(seed)

        self.db.commit()
        self.db.close()
