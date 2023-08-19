from fastapi import FastAPI, Depends, status, HTTPException, APIRouter, Response
from typing import List
from sqlalchemy.orm import Session
import schemas, models, database
from repository import blog

router = APIRouter(tags=["Blog"], prefix="/blog")

get_db = database.get_db

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------Blogs API---------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


@router.post("/", status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ShowBlog],
)
def getAll(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
def getOne(id, response: Response, db: Session = Depends(get_db)):
    return blog.get_one(id, response, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteOne(id, db: Session = Depends(get_db)):
    return blog.delete_one(id, db)
