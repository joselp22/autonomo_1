from sqlalchemy.orm import Session

from app import models
from app import schemas


def listar_productos(db: Session):
    return db.query(models.Producto).all()


def crear_producto(db: Session, producto: schemas.ProductoCreate):

    nuevo = models.Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        descripcion=producto.descripcion
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo