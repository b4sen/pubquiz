from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.controllers import team as tc
from pubquiz.dependencies import get_db

router = APIRouter(prefix="/team")


@router.get("/team/{team_hash}", response_model=schemas.Team | None)
def get_team(team_hash: str, db: Session = Depends(get_db)):
    return tc.get_team(db, team_hash)


@router.post("/team", response_model=schemas.Team | None)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    obj = tc.create_team(db, team)
    return obj


@router.post("/team/{team_hash}", response_model=schemas.Team | None)
def add_member(
    team_hash: str, member: schemas.MemberCreate, db: Session = Depends(get_db)
):
    return tc.add_member(db, team_hash, member)
