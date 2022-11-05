from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.models import Question, Quiz


def create_question(db: Session, question: schemas.QuestionCreate, quiz_id: int):
    db_question = Question(**question.dict(exclude={"quiz_id"}))
    db_quiz = db.query(Quiz).get(quiz_id)
    db_quiz.questions.append(db_question)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz


def get_question(db: Session, id: int):
    db_question = db.query(Question).get(id)
    return db_question


def delete_question(db: Session, id: int):
    db_question = db.query(Question).get(id)
    db.delete(db_question)
    db.commit()
    return db_question


def update_question(db: Session, question: schemas.QuestionUpdate, id: int):
    db_question = get_question(db, id)
    if not db_question:
        return None
    data = question.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_question, key, value)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
