
from app.database.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")



DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME,
)

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    Base.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session