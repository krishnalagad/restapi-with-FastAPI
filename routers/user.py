from fastapi import FastAPI, Depends, status, HTTPException, APIRouter, Response
from typing import List
from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas, database

router = APIRouter(
    tags=['User'],
    prefix='/user'
)

get_db = database.get_db

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------User API---------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
    
)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
    
)
def getUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} is not found in db",
        )
    return user


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ShowUser],
    
)
def getUsers(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
