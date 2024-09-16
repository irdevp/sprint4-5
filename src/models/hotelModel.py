from sqlmodel import SQLModel, Field
from typing import Optional


class Reserva(SQLModel, table=True):
    __tablename__ = "reservas_modificadas"
    id: Optional[int] = Field(default=None, primary_key=True)
    no_of_adults: int 
    no_of_children: int
    type_of_meal_plan: str 
    avg_price_per_room: float
    label_avg_price_per_room: int 