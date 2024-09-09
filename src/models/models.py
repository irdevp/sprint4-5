from sqlmodel import SQLModel, Field
from typing import Optional

class Carro(SQLModel, table=True):
    __tablename__ = 'carros'  # Adicione esta linha para especificar o nome da tabela

    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    ano: int
