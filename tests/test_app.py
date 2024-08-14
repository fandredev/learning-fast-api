from http import HTTPStatus

from fastapi.testclient import TestClient

from learning_fast_api.app import app


def test_read_root_should_return_OK_and_hello_world():
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}
