from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import parse_obj_as

from pubquiz import schemas
from pubquiz.db.controllers import quiz as qc
from pubquiz.dependencies import get_db

router = APIRouter(prefix="/quiz", tags=["quiz endpoints"])


@router.get("/", response_model=list[schemas.QuizDisplay] | None)
def get_quizes(db: Session = Depends(get_db)):
    return qc.get_quizes(db)


@router.get("/{quiz_id}")
def get_quiz_by_id(quiz_id: int, db: Session = Depends(get_db)):
    quiz = qc.get_quiz_by_id(db, quiz_id)
    now = datetime.now()
    if quiz.ends_at > now:
        quiz = parse_obj_as(schemas.QuizDisplay, quiz)
    else:
        quiz = parse_obj_as(schemas.Quiz, quiz)
    return quiz


@router.post("/{quiz_id}/register/{team_hash}")
def register_team(quiz_id: int, team_hash: str, db: Session = Depends(get_db)):
    return qc.register_team(db, quiz_id, team_hash)


@router.get("/{quiz_id}/{team_hash}")
def get_quiz_questions(quiz_id: int, team_hash: str, db: Session = Depends(get_db)):
    pass
