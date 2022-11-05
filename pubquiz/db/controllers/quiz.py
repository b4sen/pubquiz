from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.models import Quiz, Team


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


def delete_quiz(db: Session, id: int):
    db_quiz = db.query(Quiz).get(id)
    db.delete(db_quiz)
    db.commit()
    return db_quiz


def register_team(db: Session, quiz_id: int, team_hash: str):
    db_team = db.query(Team).where(Team.hash == team_hash).first()
    db_quiz = db.query(Quiz).get(quiz_id)
    if not db_team or not db_quiz:
        return None
    db_quiz.teams_registered.append(db_team)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz


def edit_quiz(db: Session, quiz_id: int, quiz: schemas.QuizEdit):
    db_quiz = get_quiz_by_id(db, quiz_id)
    if not db_quiz:
        return None
    data = quiz.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_quiz, key, value)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz
