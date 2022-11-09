from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from pubquiz import schemas
from pubquiz.dependencies import get_db
from pubquiz.db.controllers import quiz as qc

router = APIRouter(prefix="/quiz", tags=["quiz endpoints"])


@router.get("/", response_model=list[schemas.QuizDisplay])
def get_quizes(db: Session = Depends(get_db)):
    return qc.get_quizes(db)


@router.get("/{quiz_id}", response_model=schemas.QuizDisplay | None)
def get_quiz_by_id(quiz_id: int, db: Session = Depends(get_db)):
    return qc.get_quiz_by_id(db, quiz_id)


@router.post("/{quiz_id}/register/{team_hash}")
def register_team(quiz_id: int, team_hash: str, db: Session = Depends(get_db)):
    return qc.register_team(db, quiz_id, team_hash)
