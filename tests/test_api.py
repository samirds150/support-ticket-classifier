from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_category():
    response = client.post("/predict", json={"text": "I want to cancel my subscription"})
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert data["category"] in [
        "Billing",
        "Technical Issue",
        "Cancellation",
        "General Query",
        "Feedback"
    ]
