# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
# * Чтение всех
# * Чтение одного
# * Запись
# * Изменение
# * Удаление




# main.py
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends, FastAPI, HTTPException, status
from models import DATABASE_URL, engine, Base, User, Item, Order, UserCreate, UserRead, ItemCreate, ItemRead, OrderCreate, OrderRead, SessionLocal
import pandas as pd
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    item_id: int
    order_date: datetime
    status: str

@app.get("/users/all")
def read_all_users(request: Request, db: Session = SessionLocal()):
    users = db.query(User).all()
    users_df = pd.DataFrame.from_records([user.__dict__ for user in users])
    
    return templates.TemplateResponse("table.html", {
        "request": request,
        "title": "Users Table",
        "table": users_df.to_html(classes="table table-striped table-hover")
    })

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return UserResponse(**db_user.__dict__)

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(**user.__dict__)

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in user.dict().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    db.close()
    return UserResponse(**db_user.__dict__)

@app.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    db.close()
    return UserResponse(**db_user.__dict__)

@app.get("/items/all")
def read_all_items(request: Request, db: Session = SessionLocal()):
    items = db.query(Item).all()
    items_df = pd.DataFrame.from_records([item.__dict__ for item in items])
    
    return templates.TemplateResponse("table.html", {
        "request": request,
        "title": "Items Table",
        "table": items_df.to_html(classes="table table-striped table-hover")
    })

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    db = SessionLocal()
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return ItemResponse(**db_item.__dict__)

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(**db_item.__dict__)

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        db.close()
        raise HTTPException(status_code=404, detail="Item not found")
    for field, value in item.dict().items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    db.close()
    return ItemResponse(**db_item.__dict__)

@app.delete("/items/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        db.close()
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    db.close()
    return ItemResponse(**db_item.__dict__)

@app.get("/orders/all")
def read_all_orders(request: Request, db: Session = SessionLocal()):
    orders = db.query(Order).all()
    orders_df = pd.DataFrame.from_records([order.__dict__ for order in orders])
    
    return templates.TemplateResponse("table.html", {
        "request": request,
        "title": "Orders Table",
        "table": orders_df.to_html(classes="table table-striped table-hover")
    })

@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    db = SessionLocal()
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    db.close()
    return OrderResponse(**db_order.__dict__)

@app.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int):
    db = SessionLocal()
    db_order = db.query(Order).filter(Order.id == order_id).first()
    db.close()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderResponse(**db_order.__dict__)

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderCreate):
    db = SessionLocal()
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")
    for field, value in order.dict().items():
        setattr(db_order, field, value)
    db.commit()
    db.refresh(db_order)
    db.close()
    return OrderResponse(**db_order.__dict__)

@app.delete("/orders/{order_id}", response_model=OrderResponse)
def delete_order(order_id: int):
    db = SessionLocal()
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    db.close()
    return OrderResponse(**db_order.__dict__)
