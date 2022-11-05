from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.controllers import question as question_c
from pubquiz.db.controllers import quiz as qc
from pubquiz.dependencies import get_db

router = APIRouter(prefix="/quiz")


@router.get("/", response_model=list[schemas.Quiz | None])
def get_quizes(db: Session = Depends(get_db)):
    return qc.get_quizes(db)


@router.get("/{quiz_id}", response_model=schemas.Quiz | None)
def get_quiz_by_id(quiz_id: int, db: Session = Depends(get_db)):
    quiz = qc.get_quiz_by_id(db, quiz_id)
    return quiz


@router.post("/", response_model=schemas.Quiz)
def create_quiz(quiz: schemas.QuizCreate, db: Session = Depends(get_db)):
    q = qc.create_quiz(db, quiz)
    return q


@router.delete("/{quiz_id}", response_model=schemas.Quiz)
def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    q = qc.delete_quiz(db, quiz_id)
    return q


@router.post("/{quiz_id}/question", response_model=schemas.Quiz)
def add_question(
    quiz_id: int, question: schemas.QuestionCreate, db: Session = Depends(get_db)
):
    return question_c.create_question(db, question, quiz_id)


@router.post("/{quiz_id}/register/{team_hash}", response_model=schemas.Quiz)
def register_team(quiz_id: int, team_hash: str, db: Session = Depends(get_db)):
    return qc.register_team(db, quiz_id, team_hash)
