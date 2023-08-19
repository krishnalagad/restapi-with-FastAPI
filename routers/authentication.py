from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models, jwttoken
from sqlalchemy.orm import Session
from hashing import Hash
from datetime import datetime, timedelta

router = APIRouter(tags=["Auth"])
get_db = database.get_db


@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect Username",
        )

    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect Password",
        )

    # generate jwt token here and return it.
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwttoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
