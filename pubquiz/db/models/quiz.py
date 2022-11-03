from sqlalchemy import Column, DateTime, ForeignKey, String, Table, func
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import NotNull

quiz_teams = Table(
    "registered_teams",
    Base.metadata,
    Column("quiz_id", ForeignKey("quiz.id")),
    Column("team_id", ForeignKey("team.id")),
)

quiz_questions = Table(
    "quiz_questions",
    Base.metadata,
    Column("quiz_id", ForeignKey("quiz.id")),
    Column("question_id", ForeignKey("questions.id")),
)


class Quiz(Base):
    __tablename__ = "quiz"

    quiz_name = NotNull(String, unique=True)
    created_at = NotNull(DateTime, server_default=func.now())
    starts_at = NotNull(DateTime)
    ends_at = Column(DateTime)
    teams_registered = relationship(
        "Team", secondary=quiz_teams, back_populates="quizes", cascade="all"
    )
    questions = relationship(
        "Question",
        secondary=quiz_questions,
        cascade="all, delete-orphan",
        single_parent=True,
    )
