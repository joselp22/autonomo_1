from pydantic import BaseModel
from pydantic import ConfigDict


class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    descripcion: str


class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    descripcion: str

    model_config = ConfigDict(from_attributes=True)