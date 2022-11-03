from datetime import datetime

from pydantic import BaseModel


class Quiz(BaseModel):
    id: int
    quiz_name: str
    starts_at: datetime
    ends_at: datetime | None = None
    teams_registered: list | None = []
    questions: list | None = []

    class Config:
        orm_mode = True


class QuizCreate(BaseModel):
    quiz_name: str
    starts_at: datetime
    ends_at: datetime | None = None
