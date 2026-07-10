from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "API funcionando correctamente"
    }


def test_listar_productos():
    response = client.get("/productos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_producto():
    producto = {
        "nombre": "Teclado",
        "precio": 25.99,
        "descripcion": "Teclado mecánico básico"
    }

    response = client.post(
        "/productos/crear",
        json=producto
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["nombre"] == "Teclado"
    assert data["precio"] == 25.99
    assert data["descripcion"] == "Teclado mecánico básico"


def test_obtener_producto():
    producto = {
        "nombre": "Mouse",
        "precio": 15.50,
        "descripcion": "Mouse inalámbrico"
    }

    crear_response = client.post(
        "/productos/crear",
        json=producto
    )

    producto_id = crear_response.json()["id"]

    response = client.get(
        f"/productos/{producto_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == producto_id
    assert response.json()["nombre"] == "Mouse"


def test_obtener_producto_no_existente():
    response = client.get("/productos/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }


def test_actualizar_producto():
    producto = {
        "nombre": "Monitor",
        "precio": 300.00,
        "descripcion": "Monitor de 24 pulgadas"
    }

    crear_response = client.post(
        "/productos/crear",
        json=producto
    )

    producto_id = crear_response.json()["id"]

    producto_actualizado = {
        "nombre": "Monitor actualizado",
        "precio": 350.00,
        "descripcion": "Monitor Full HD de 27 pulgadas"
    }

    response = client.put(
        f"/productos/actualizar/{producto_id}",
        json=producto_actualizado
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == producto_id
    assert data["nombre"] == "Monitor actualizado"
    assert data["precio"] == 350.00
    assert data["descripcion"] == "Monitor Full HD de 27 pulgadas"


def test_actualizar_producto_no_existente():
    producto = {
        "nombre": "Producto inexistente",
        "precio": 100.00,
        "descripcion": "Este producto no existe"
    }

    response = client.put(
        "/productos/actualizar/999999",
        json=producto
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }


def test_eliminar_producto():
    producto = {
        "nombre": "Audífonos",
        "precio": 45.00,
        "descripcion": "Audífonos Bluetooth"
    }

    crear_response = client.post(
        "/productos/crear",
        json=producto
    )

    producto_id = crear_response.json()["id"]

    response = client.delete(
        f"/productos/eliminar/{producto_id}"
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Producto eliminado correctamente",
        "id": producto_id
    }

    consultar_response = client.get(
        f"/productos/{producto_id}"
    )

    assert consultar_response.status_code == 404


def test_eliminar_producto_no_existente():
    response = client.delete(
        "/productos/eliminar/999999"
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }


def test_crear_producto_invalido():
    producto = {
        "nombre": "Producto inválido",
        "precio": "precio_incorrecto",
        "descripcion": "Producto con precio incorrecto"
    }

    response = client.post(
        "/productos/crear",
        json=producto
    )

    assert response.status_code == 422