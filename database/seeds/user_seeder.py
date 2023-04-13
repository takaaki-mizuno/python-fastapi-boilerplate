from injector import Injector, inject
from .base_seeder import BaseSeeder
from app.models import User


class UserSeeder(BaseSeeder):
    model = User

    def get_data(self) -> list:
        return [
            {'name': 'Test User', 'email': 'test@example.com', 'password': self.hash.generate_hash("test")},
        ]
