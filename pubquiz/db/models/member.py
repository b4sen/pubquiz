from sqlalchemy import String, Integer, ForeignKey

from .base import Base
from .mixins import NotNull


class Member(Base):

    __tablename__ = "member"
    member_name = NotNull(String, unique=True)
    team = NotNull(Integer, ForeignKey("team.id"))
