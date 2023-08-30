from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from config.db import Base, SessionLocale, engine, get_db
from models.model import Users
from sqlalchemy.orm import Session

from schema.user import UserShowSchema, UserCreateSchema


router = APIRouter(tags=['User'], prefix = '/user')


@router.get("/", response_model=List[UserShowSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(Users).all()


@router.post("/", response_model=UserShowSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    u = Users(name=user.name, email=user.email, password=user.password)
    db.add(u)
    db.commit()
    return u

@router.get('/{id}', response_model=UserShowSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(Users).where(Users.id == id).first()

@router.put('/{id}', response_model=UserShowSchema)
def update_user(id: int, user: UserShowSchema, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == id).first()
        u.name = user.name
        u.email = user.email
        db.add(u)
        db.commit()
        return u
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
@router.delete('/{id}', response_class=JSONResponse)
def delete_user(id: int, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == id).first()
        db.delete(u)
        db.commit()
        return {f'User of id {id} has been deleted successfully': True}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")