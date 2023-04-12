from typing import Optional, Tuple

from injector import Injector, inject

from ..libraries import Hash
from ..models import User
from ..repositories import UserRepository


class UserService(object):

    @inject
    def __init__(self, user_repository: UserRepository, _hash: Hash):
        self._user_repository = user_repository
        self._hash = _hash

    def sign_in(self, email: str, password: str) -> Optional[Tuple[User, str]]:
        user = self._user_repository.get_by_email(email)

        if user is None:
            return None

        if self._hash.check_hash(user.password, password):
            return user, self._hash.generate_hash(user.ID)

        return None
