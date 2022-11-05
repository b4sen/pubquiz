from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.controllers import team as tc
from pubquiz.dependencies import get_db

router = APIRouter(prefix="/team")


@router.get("/", response_model=list[schemas.Team | None])
def get_teams(db: Session = Depends(get_db)):
    return tc.get_teams(db)


@router.get("/{team_id}", response_model=schemas.Team | None)
def get_team(team_id: int, db: Session = Depends(get_db)):
    return tc.get_team_by_id(db, team_id)


@router.post("/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    obj = tc.create_team(db, team)
    return obj


@router.delete("/{team_id}", response_model=schemas.Team | None)
def delete_team(team_id: int, db: Session = Depends(get_db)):
    obj = tc.delete_team(db, team_id)
    return obj


@router.post("/{team_id}", response_model=schemas.Team)
def add_member(
    team_id: int, member: schemas.MemberCreate, db: Session = Depends(get_db)
):
    return tc.add_member_admin(db, team_id, member)


@router.delete("/{team_id}/{member_id}", response_model=schemas.Team | None)
def remove_member(team_id: int, member_id: int, db: Session = Depends(get_db)):
    return tc.remove_member(db, team_id, member_id)
