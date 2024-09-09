from sqlmodel import SQLModel, Field
from typing import Optional

class Carro(SQLModel, table=True):
    __tablename__ = 'carros' 

    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    ano: int
