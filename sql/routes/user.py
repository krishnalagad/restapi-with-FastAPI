from fastapi import APIRouter, Depends, status
from sql.config.db import conn
from sql.schema.user import User
from sqlalchemy.orm import Session
from sql.models.user import users

router = APIRouter(tags=["User"], prefix="/user")


@router.get("/")
async def get_all():
    return conn.execute(users.select()).fetchall()


@router.get("/{id}")
async def get_one(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@router.post("/")
async def create(user: User):
    conn.execute(
        users.insert().values(name=user.name, email=user.email, password=user.password)
    )
    return conn.execute(users.select()).fetchall()


@router.put("/{id}")
async def update(id: int, user: User):
    conn.execute(
        users.update()
        .values(name=user.name, email=user.email, password=user.password)
        .where(users.c.id == id)
    )
    return conn.execute(users.select()).fetchall()


@router.delete("/{id}")
async def delete(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create(user: User, db: Session = Depends(get_db)):
#     new_user = modelUser.User(name=user.name, email=user.email, password=user.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
