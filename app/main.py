from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import crud
from app import models
from app import schemas
from app.database import Base
from app.database import engine
from app.database import get_db


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API REST de Productos",
    description="API desarrollada con FastAPI y PostgreSQL",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "API funcionando correctamente"
    }


@app.get(
    "/productos",
    response_model=list[schemas.ProductoResponse],
)
def listar_productos(
    db: Session = Depends(get_db),
):
    return crud.listar_productos(db)


@app.get(
    "/productos/{producto_id}",
    response_model=schemas.ProductoResponse,
)
def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db),
):
    producto = (
        db.query(models.Producto)
        .filter(models.Producto.id == producto_id)
        .first()
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto


@app.post(
    "/productos/crear",
    response_model=schemas.ProductoResponse,
    status_code=201,
)
def crear_producto(
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db),
):
    return crud.crear_producto(
        db=db,
        producto=producto,
    )


@app.put(
    "/productos/actualizar/{producto_id}",
    response_model=schemas.ProductoResponse,
)
def actualizar_producto(
    producto_id: int,
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db),
):
    producto_db = (
        db.query(models.Producto)
        .filter(models.Producto.id == producto_id)
        .first()
    )

    if producto_db is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    producto_db.nombre = producto.nombre
    producto_db.precio = producto.precio
    producto_db.descripcion = producto.descripcion

    db.commit()
    db.refresh(producto_db)

    return producto_db


@app.delete(
    "/productos/eliminar/{producto_id}",
)
def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db),
):
    producto = (
        db.query(models.Producto)
        .filter(models.Producto.id == producto_id)
        .first()
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    db.delete(producto)
    db.commit()

    return {
        "message": "Producto eliminado correctamente",
        "id": producto_id,
    }