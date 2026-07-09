from fastapi import Depends
from fastapi import FastAPI

from sqlalchemy.orm import Session

from app.database import Base
from app.database import engine
from app.database import get_db

from app import crud
from app import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Productos",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}


@app.get("/productosget", response_model=list[schemas.ProductoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_productos(db)


@app.post(
    "/productos",
    response_model=schemas.ProductoResponse,
    status_code=201
)
def crear(
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db, producto)