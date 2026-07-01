from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_openapi_available():
    response = client.get("/openapi.json")
    assert response.status_code == 200


def test_usuario_crud():
    payload = {"nome": "sample", "email": "sample", "senhaHash": "sample"}
    created = client.post("/api/usuarios", json=payload)
    assert created.status_code == 201, created.text
    item = created.json()
    listed = client.get("/api/usuarios")
    assert listed.status_code == 200
    assert item["id"] in [row["id"] for row in listed.json()]
