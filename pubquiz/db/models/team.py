from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import NotNull
from .quiz import quiz_teams

# TODO: remove, unused
assoc_table = Table(
    "team_members",
    Base.metadata,
    Column("team_id", ForeignKey("team.id")),
    Column("member_id", ForeignKey("member.id")),
)


class Team(Base):

    __tablename__ = "team"

    team_name = NotNull(String, unique=True)
    captain_name = NotNull(String)
    hash = NotNull(String)
    members = relationship(
        "Member",
        cascade="all, delete-orphan",
        single_parent=True,
    )
    quizes = relationship(
        "Quiz", secondary=quiz_teams, back_populates="teams_registered"
    )
    answers = relationship(
        "TeamAnswers", single_parent=True, cascade="all, delete-orphan"
    )


class TeamAnswers(Base):

    __tablename__ = "team_answers"
    team_id = NotNull(Integer, ForeignKey("team.id"))
    quiz_id = NotNull(Integer, ForeignKey("quiz.id"))
    question_id = NotNull(Integer, ForeignKey("questions.id"))
    answer = NotNull(String)
