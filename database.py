from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config as env

engine = create_engine(env("DB_URL"), echo=True)


Base = declarative_base()
session = sessionmaker()
