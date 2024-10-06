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

    orders = relationship("Order", back_populates="user")  # one-to-many relationship

    def __repr__(self):
        return f"<User {self.username}>"


class Order(Base):
    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("SHIPPED", "shipped"),
        ("DELIVERED", "delivered"),
    )

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=0)
    status = Column(ChoiceType(ORDER_STATUS), default="PENDING")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="orders")  # many-to-one relationship
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="orders")  # many-to-one relationship

    def __repr__(self):
        return f"<Order {self.id}>"


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Integer)

    orders = relationship("Order", back_populates="product")  # one-to-many relationship

    def __repr__(self):
        return f"<Product {self.name}>"
