from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product_endpoint():
    response = client.post("/products/", json={"name": "Celular", "price": 3000})
    assert response.status_code == 201
    assert "id" in response.json()
