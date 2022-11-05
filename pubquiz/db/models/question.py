from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import NotNull


class Question(Base):
    __tablename__ = "questions"
    quiz_id = Column(String(16), ForeignKey("quiz.id"))
    title = NotNull(String, unique=True)
    answer = NotNull(
        String,
        comment="if is_guess is true, this is the correct answer"
        ", else the number of the answer",
    )
    img_url = Column(String)
