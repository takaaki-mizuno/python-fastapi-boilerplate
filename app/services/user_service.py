from typing import Optional, Tuple

import jwt
from injector import Injector, inject

from ..config import Config
from ..libraries import Hash
from ..models import User
from ..repositories import UserRepository


class UserService(object):

    @inject
    def __init__(self, user_repository: UserRepository, _hash: Hash,
                 config: Config):
        self._user_repository = user_repository
        self._hash = _hash
        self._config = config

    def sign_in(self, email: str, password: str) -> Optional[Tuple[User, str]]:
        user = self._user_repository.get_by_email(email)

        if user is None:
            return None

        if self._hash.check_hash(password, user.password):
            return user, self.generate_access_token(str(user.id))

        return None

    def generate_access_token(self, user_id: str) -> str:
        encoded_jwt = jwt.encode({"user_id": user_id},
                                 self._config.JWT_SECRET,
                                 algorithm=self._config.JWT_ALGORITHM)
        return encoded_jwt

    def get_user_by_token(self, access_token: str) -> Optional[User]:
        a = access_token.encode("utf-8")
        try:
            print(access_token)
            decoded_jwt = jwt.decode(a,
                                     self._config.JWT_SECRET,
                                     algorithms=[self._config.JWT_ALGORITHM])
        except jwt.exceptions.DecodeError as e:
            print(e)
            return None

        user = self._user_repository.get(decoded_jwt["user_id"])

        return user
