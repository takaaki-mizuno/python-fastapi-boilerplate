import time

from sqlalchemy.orm import declarative_base


def current_time() -> int:
    return round(time.time())


Base = declarative_base()
