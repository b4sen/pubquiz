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


@router.delete("/{question_id}", response_model=schemas.Question | None)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    return qc.delete_question(db, question_id)


@router.put("/{question_id}", response_model=schemas.Question | None)
def update_question(
    question_id: int, question: schemas.QuestionUpdate, db: Session = Depends(get_db)
):
    return qc.update_question(db, question, question_id)
