import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index_returns_ok(client):
    r = client.get("/")
    data = r.get_json()
    assert r.status_code == 200
    assert data["status"] == "ok"
    assert data["message"] == "hello from opsera this a full devsecops project"


def test_health_returns_200(client):
    r = client.get("/health")
    assert r.status_code == 200
