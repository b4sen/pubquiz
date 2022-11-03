from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.controllers import question as qc
from pubquiz.dependencies import get_db

router = APIRouter(prefix="/question")


@router.post("/")
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    qc.create_question(db, question)


@router.get("/{question_id}", response_model=schemas.Question | None)
def get_question(question_id: int, db: Session = Depends(get_db)):
    return qc.get_question(db, question_id)
