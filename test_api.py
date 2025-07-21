from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_submit_data():
    response = client.post("/submitData", json={
        "beauty_title": "пер.",
        "title": "Тестовый перевал",
        "other_titles": "альтернативное",
        "user": {
            "email": "test@example.com",
            "phone": "+79999999999",
            "fam": "Иванов",
            "name": "Иван",
            "otc": "Иванович"
        }
    })
    assert response.status_code == 200
    assert response.json()["status"] == 1
