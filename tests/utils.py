import random
import string
from datetime import datetime, timedelta

from pubquiz import schemas


def random_string(length=10):
    return "".join(random.choices(string.printable, k=length))


def create_random_quiz():
    quiz_name = random_string(10)
    starts_at = datetime.now()
    ends_at = starts_at + timedelta(hours=1)
    return schemas.QuizCreate(quiz_name=quiz_name, starts_at=starts_at, ends_at=ends_at)


def create_random_team():
    team_name = random_string(10)
    captain_name = random_string(5)
    return schemas.TeamCreate(team_name=team_name, captain_name=captain_name)


def create_random_question():
    title = random_string(10)
    answer = random_string(3)
    img_url = random_string(20)
    return schemas.QuestionCreate(title=title, answer=answer, img_url=img_url)
