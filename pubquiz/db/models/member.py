from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import NotNull
from .team import assoc_table as team_member


class Member(Base):

    __tablename__ = "member"
    member_name = NotNull(String, unique=True)
    teams = relationship(
        "Team", secondary=team_member, back_populates="members", cascade="all"
    )
