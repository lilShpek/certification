from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

    user = relationship("User", back_populates="orders")
    item = relationship("Item", back_populates="orders")

User.orders = relationship("Order", back_populates="user")
Item.orders = relationship("Order", back_populates="item")

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserRead(UserCreate):
    id: int

class ItemCreate(BaseModel):
    name: str
    description: str
    price: int

class ItemRead(ItemCreate):
    id: int

class OrderCreate(BaseModel):
    user_id: int
    item_id: int
    status: str

class OrderRead(OrderCreate):
    id: int
    order_date: datetime
