from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_empresa():
    response = client.post("/empresas/", json={"nome": "Empresa XYZ", "cnpj": "12345678000195", "endereco": "Rua A", "email": "contato@empresa.com", "telefone": "123456789"})
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa XYZ"
