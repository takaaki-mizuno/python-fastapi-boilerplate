from app.bootstrap.container import build_container
from .user_seeder import UserSeeder


def seed():
    _injector = build_container()
    UserSeeder(_injector).run()

