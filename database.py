from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from main import env

engine = create_engine(env("DB_URL"), echo=True)


Base = declarative_base()
Session = sessionmaker()
