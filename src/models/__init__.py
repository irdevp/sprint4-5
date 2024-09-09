from sqlmodel import SQLModel
from core.db import engine

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  # Cria as tabelas no banco de dados
