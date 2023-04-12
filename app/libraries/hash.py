import bcrypt


class Hash(object):

    def __int__(self):
        pass

    @staticmethod
    def generate_hash(key: str) -> str:
        _byte_key = key.encode('utf-8')
        salt = bcrypt.gensalt()
        _hash = bcrypt.hashpw(_byte_key, salt)
        return _hash.decode('utf-8')

    @staticmethod
    def check_hash(key: str, _hash: str) -> bool:
        _byte_key = key.encode('utf-8')
        _byte_hash = _hash.encode('utf-8')
        return bcrypt.checkpw(_byte_key, _byte_hash)
