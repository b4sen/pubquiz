from pydantic import BaseModel


class Question(BaseModel):
    title: str
    is_guess: bool
    quiz_id: int
    answer: str | int
    answer_1: str | None = None
    answer_2: str | None = None
    answer_3: str | None = None
    answer_4: str | None = None

    class Config:
        orm_mode = True


class QuestionCreate(Question):
    pass
