from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric

from app.database import Base


class Producto(Base):

    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String(100), nullable=False)

    precio = Column(Numeric(10, 2), nullable=False)

    descripcion = Column(String(500), nullable=False)