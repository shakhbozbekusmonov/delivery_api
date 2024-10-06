from database import Base, engine
from models import User, Product, Order

Base.metadata.create_all(bind=engine)
