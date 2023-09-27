import pytest
from fastapi.testclient import TestClient
from api.my_api import app


@pytest.fixture
def client():
    return TestClient(app)


def test_login(client):
    response = client.get("/test/1/2")
    assert response.status_code == 200
    assert response.json() == 3
