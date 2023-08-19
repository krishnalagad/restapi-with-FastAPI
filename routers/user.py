from fastapi import FastAPI, Depends, status, HTTPException, APIRouter, Response
from typing import List
from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas, database
from repository import user

router = APIRouter(tags=["User"], prefix="/user")

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
    return user.create(request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
)
def getUser(id: int, db: Session = Depends(get_db)):
    return user.get_one(id, db)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ShowUser],
)
def getUsers(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
