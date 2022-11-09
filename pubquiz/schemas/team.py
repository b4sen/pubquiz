from collections import defaultdict

from pydantic import BaseModel, Extra, validator

from .member import MemberBase


class TeamCreate(BaseModel, extra=Extra.allow):
    team_name: str
    captain_name: str


class TeamAnswer(BaseModel):
    quiz_id: int
    question_id: int
    answer: str

    class Config:
        orm_mode = True


class TeamAnswerUpdate(BaseModel):
    answer_id: int
    answer: str


class Answer(BaseModel):
    question_id: int
    answer: str


class TeamQuizAnswers(BaseModel):
    quiz_id: int
    answers: list[Answer] = []


class Team(BaseModel):
    id: int
    team_name: str
    captain_name: str
    hash: str
    members: list[MemberBase]
    quizes: list
    answers: list[TeamQuizAnswers] | None  # swagger shows schema before validation

    class Config:
        orm_mode = True

    @validator("answers", pre=True)
    def group_keys(cls, v):
        res = defaultdict(list)
        for answer in v:
            quiz_id = answer.quiz_id
            data = {"question_id": answer.question_id, "answer": answer.answer}
            res[quiz_id].append(data)
        out = []
        for k, v in res.items():
            out.append({"quiz_id": k, "answers": v})
        return out
