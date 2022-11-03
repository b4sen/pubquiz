from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import NotNull
from .quiz import quiz_teams

assoc_table = Table(
    "team_members",
    Base.metadata,
    Column("team_id", ForeignKey("team.id")),
    Column("member_id", ForeignKey("member.id")),
)


class Team(Base):

    __tablename__ = "team"

    team_name = NotNull(String, unique=True)
    captain_id = NotNull(Integer, ForeignKey("member.id"))
    members = relationship(
        "Member", secondary=assoc_table, back_populates="teams", cascade="all"
    )
    quizes = relationship(
        "Quiz", secondary=quiz_teams, back_populates="teams_registered", cascade="all"
    )
