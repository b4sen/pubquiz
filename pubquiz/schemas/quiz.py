from datetime import datetime

from pydantic import BaseModel, validator

from .question import Question
from .member import MemberBase


class QuizTeam(BaseModel):
    id: int
    team_name: str
    captain_name: str
    members: list[MemberBase] | None = []

    class Config:
        orm_mode = True


class Quiz(BaseModel):
    id: int
    quiz_name: str
    starts_at: datetime
    ends_at: datetime | None = None
    teams_registered: list[QuizTeam] | None = []
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


class QuizDisplay(BaseModel):
    id: int
    quiz_name: str
    starts_at: datetime
    ends_at: datetime | None = None
    teams_registered: int = 0

    @validator("teams_registered", pre=True)
    def count_teams_registered(cls, v):
        return len(v)

    class Config:
        orm_mode = True
