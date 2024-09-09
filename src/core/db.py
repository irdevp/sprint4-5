from sqlmodel import create_engine
from core.config import Config

engine = create_engine(Config.DATABASE_URL, echo=True)
