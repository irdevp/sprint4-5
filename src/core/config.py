import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL')#dados do banco
    if not DATABASE_URL:
        raise ValueError("A variável de ambiente 'DATABASE_URL' não está definida.")
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Chave secreta para sessão do Flask
