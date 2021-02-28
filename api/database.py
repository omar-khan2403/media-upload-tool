from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('POSTGRES_USER')
pw = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{pw}@127.0.0.1:5432/{db}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
