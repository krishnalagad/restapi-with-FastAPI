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
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found in db",
        )
    blog.update(request.model_dump())  # dict() is deprecated, so use model_dump()
    db.commit()
    return "Updated"


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
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found in db",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} is not found in db'}
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteOne(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found in db",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Done!!"}
