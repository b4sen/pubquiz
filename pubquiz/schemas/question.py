from pydantic import BaseModel


class Question(BaseModel):
    id: int
    title: str
    answer: str | int
    img_url: str | None = None

    class Config:
        orm_mode = True


class QuestionCreate(Question):
    pass


class QuestionUpdate(BaseModel):
    title: str | None = None
    answer: str | int | None = None
    img_url: str | None = None


class QuestionDisplay(BaseModel):
    id: int
    title: str
    img_url: str | None
