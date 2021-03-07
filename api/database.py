from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('POSTGRES_USER')
pw = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{pw}@{host}:{port}/{db}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
