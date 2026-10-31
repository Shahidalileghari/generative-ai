from fastapi.testclient import TestClient
from examples.api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_demo_generation():
    response = client.post("/generate-demo", json={"prompt": "Explain attention"})
    assert response.status_code == 200
    body = response.json()
    assert body["demo"] is True
    assert body["model"] == "deterministic-demo"
    assert "17 characters" in body["output"]

def test_empty_prompt_rejected():
    assert client.post("/generate-demo", json={"prompt": ""}).status_code == 422
