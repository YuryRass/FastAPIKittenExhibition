from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_breeds():
    response = client.get("/breeds/")
    assert response.status_code == 200


def test_get_kittens():
    response = client.get("/kittens/")
    assert response.status_code == 200


def test_create_kitten():
    response = client.post(
        "/kittens/",
        json={
            "name": "Fluffy",
            "color": "white",
            "age": 3,
            "description": "Cute kitten",
            "breed_id": 1,
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Fluffy"
