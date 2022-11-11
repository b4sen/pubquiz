from fastapi.encoders import jsonable_encoder

from pubquiz.db.controllers import quiz as qc
from pubquiz.db.controllers import team as tc
from tests.utils import (create_random_question, create_random_quiz,
                         create_random_team)


def test_get_quizes_client(client):
    response = client.get("/api/admin/quiz/")
    assert response.status_code == 401, response.text


def test_get_quizes_admin(admin):
    response = admin.get("/api/admin/quiz/")
    assert response.status_code == 200, response.text


def test_get_quiz_by_id_client(client, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    response = client.get(f"/api/admin/quiz/{q.id}")
    assert response.status_code == 401, response.text


def test_get_quiz_by_id_admin(admin, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    response = admin.get(f"/api/admin/quiz/{q.id}")
    data = response.json()
    assert response.status_code == 200, response.text
    assert data["id"] == q.id


def test_create_quiz_client(client):
    q = create_random_quiz()
    response = client.post("/api/admin/quiz/", json=jsonable_encoder(q))
    assert response.status_code == 401, response.text


def test_create_quiz_admin(admin):
    q = create_random_quiz()
    response = admin.post("/api/admin/quiz/", json=jsonable_encoder(q))
    assert response.status_code == 200, response.text


def test_delete_quiz_client(client, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    response = client.delete(f"/api/admin/quiz/{q.id}")
    assert response.status_code == 401, response.text


def test_delete_quiz_admin(admin, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    response = admin.delete(f"/api/admin/quiz/{q.id}")
    assert response.status_code == 200, response.text


def test_add_question_client(client, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    qu = create_random_question()
    res = client.post(f"/api/admin/quiz/{q.id}/question", json=jsonable_encoder(qu))
    assert res.status_code == 401, res.text


def test_add_question_admin(admin, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    qu = create_random_question()
    res = admin.post(f"/api/admin/quiz/{q.id}/question", json=jsonable_encoder(qu))
    data = res.json()
    assert res.status_code == 200, res.text
    assert len(data["questions"]) != 0


def test_register_team_client(client, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    t = create_random_team()
    t = tc.create_team(_db, t)
    res = client.post(f"/api/admin/quiz/{q.id}/register/{t.hash}")
    assert res.status_code == 401, res.text


def test_register_team_admin(admin, _db):
    q = create_random_quiz()
    q = qc.create_quiz(_db, q)
    t = create_random_team()
    t = tc.create_team(_db, t)
    res = admin.post(f"/api/admin/quiz/{q.id}/register/{t.hash}")
    data = res.json()
    assert res.status_code == 200, res.text
    assert len(data["teams_registered"]) != 0
    assert data["teams_registered"][0]["id"] == t.id
