import hashlib
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from pubquiz import schemas
from pubquiz.db.models import Team, Member


def get_team(db: Session, hash: str):
    db_team = db.query(Team).where(Team.hash == hash).first()
    return db_team


def get_team_by_id(db: Session, team_id: int):
    return db.query(Team).get(team_id)


def get_teams(db: Session):
    return db.query(Team).all()


def create_team(db: Session, team: schemas.TeamCreate):
    team.hash = hashlib.md5(team.team_name.encode()).hexdigest()
    db_team = Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

# this gets exposed to the user
def add_member(db: Session, hash: str, member: schemas.MemberCreate):
    db_team = db.query(Team).where(Team.hash == hash).first()
    if not db_team:
        return None
    db_member = Member(**member.dict())
    db_team.members.append(db_member)
    try:
        db.commit()
        db.refresh(db_team)
    except IntegrityError:
        return None  # TODO: add more verbose return value
    return db_team


def add_member_admin(db: Session, team_id: int, member: schemas.MemberCreate):
    db_team = db.query(Team).get(team_id)
    if not db_team:
        return None
    db_member = Member(**member.dict())
    db_team.members.append(db_member)
    try:
        db.commit()
        db.refresh(db_team)
    except IntegrityError:
        return None  # TODO: add more verbose return value
    return db_team


def delete_team(db: Session, team_id: int):
    db_team = db.query(Team).get(team_id)
    db.delete(db_team)
    db.commit()
    return db_team


# TODO, do i need this?
def modify_team(db: Session):
    pass


def remove_member(db: Session, team_id: int, member_id: int):
    db_member = db.query(Member).get(member_id)
    db_team = db.query(Team).get(team_id)
    if not db_member or not db_team:
        return None
    db_team.members.remove(db_member)
    db.commit()
    db.refresh(db_team)
    return db_team
