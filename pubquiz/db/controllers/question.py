from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.models import Question, Quiz


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = Question(**question.dict(exclude={'quiz_id'}))
    db_quiz = db.query(Quiz).where(Quiz.id == question.quiz_id).first()
    db_quiz.questions.append(db_question)
    db.commit()
    db.refresh(db_quiz)


def get_question(db: Session, id: int):
    db_question = db.query(Question).get(id)
    return db_question
