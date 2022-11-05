from sqlalchemy import String

from .base import Base
from .mixins import NotNull


class Admin(Base):

    __tablename__ = 'admin'
    username = NotNull(String, unique=True)
    password = NotNull(String)
