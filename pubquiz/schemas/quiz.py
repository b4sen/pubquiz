from datetime import datetime

from pydantic import BaseModel

from .question import Question


class Quiz(BaseModel):
    id: int
    quiz_name: str
    starts_at: datetime
    ends_at: datetime | None = None
    teams_registered: list | None = []
    questions: list[Question] | None = []

    class Config:
        orm_mode = True


class QuizCreate(BaseModel):
    quiz_name: str
    starts_at: datetime
    ends_at: datetime | None = None


class QuizEdit(BaseModel):
    quiz_name: str | None = None
    starts_at: datetime | None = None
    ends_at: datetime | None = None
