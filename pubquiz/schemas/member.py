from pydantic import BaseModel


class MemberBase(BaseModel):
    id: int
    member_name: str

    class Config:
        orm_mode = True


class MemberCreate(BaseModel):
    member_name: str


class Member(MemberBase):
    teams: list[str]


class MemberDelete(MemberCreate):
    pass
