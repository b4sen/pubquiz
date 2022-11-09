from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.controllers import question as qc
from pubquiz.dependencies import get_db
from pubquiz.dependencies.auth import get_current_user

router = APIRouter(prefix="/question", dependencies=[Depends(get_current_user)])


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
