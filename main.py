from fastapi import FastAPI, Depends, status, Response, HTTPException
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------Blogs API---------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


@app.post("/blog", status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
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


@app.get(
    "/blogs", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog]
)
def getAll(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
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


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
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


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------User API---------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name, email=request.email, password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
