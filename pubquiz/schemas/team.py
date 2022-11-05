from pydantic import BaseModel, Extra

from .member import MemberBase
from .quiz import Quiz


class Team(BaseModel):
    id: int
    team_name: str
    captain_name: str
    hash: str
    members: list[MemberBase]
    quizes: list[Quiz]

    class Config:
        orm_mode = True


class TeamCreate(BaseModel, extra=Extra.allow):
    team_name: str
    captain_name: str


class TeamAnswer(BaseModel):
    team_id: int
    quiz_id: int
    question_id: int
    answer: str
