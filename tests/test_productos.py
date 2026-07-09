from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "API funcionando correctamente"


def test_listar_productos():
    response = client.get("/productos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_producto():
    nuevo_producto = {
        "nombre": "Teclado",
        "precio": 25.99,
        "descripcion": "Teclado mecánico básico"
    }

    response = client.post("/productos", json=nuevo_producto)

    assert response.status_code == 201

    data = response.json()

    assert data["nombre"] == nuevo_producto["nombre"]
    assert data["precio"] == nuevo_producto["precio"]
    assert data["descripcion"] == nuevo_producto["descripcion"]
    assert "id" in data