from database import Base
from sqlalchemy import Column, Integer, Boolean, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(77), unique=True)
    password = Column(Text, nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
