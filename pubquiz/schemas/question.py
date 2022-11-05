from pydantic import BaseModel


class Question(BaseModel):
    title: str
    is_guess: bool
    answer: str | int
    answer_1: str | None = None
    answer_2: str | None = None
    answer_3: str | None = None
    answer_4: str | None = None

    class Config:
        orm_mode = True


class QuestionCreate(Question):
    pass


class QuestionUpdate(BaseModel):
    title: str | None = None
    is_guess: bool | None = None
    answer: str | int | None = None
    answer_1: str | None = None
    answer_2: str | None = None
    answer_3: str | None = None
    answer_4: str | None = None
