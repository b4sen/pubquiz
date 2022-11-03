from sqlalchemy.orm import Session

from pubquiz.db.models import Quiz
from pubquiz import schemas


def get_quizes(db: Session, limit: int = 0, offset: int = 0):
    quizes = db.query(Quiz).order_by(Quiz.starts_at).all()
    return quizes


def get_quiz_by_id(db: Session, id: int):
    return db.query(Quiz).where(Quiz.id == id).first()


def create_quiz(db: Session, quiz: schemas.QuizCreate):
    db_quiz = Quiz(**quiz.dict())
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz
