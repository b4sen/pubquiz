def test_get_quizes_client(client):
    response = client.get('/api/admin/quiz/')
    assert response.status_code == 401, response.text


def test_get_quizes_admin(admin):
    response = admin.get('/api/admin/quiz/')
    assert response.status_code == 200, response.text
