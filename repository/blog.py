import models
from sqlalchemy.orm import Session
from schemas import Blog
from fastapi import HTTPException, status, Response


def create(request: Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id, request: Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found in db",
        )
    blog.update(request.model_dump())  # dict() is deprecated, so use model_dump()
    db.commit()
    return "Updated"


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_one(id, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found in db",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} is not found in db'}
    return blog


def delete_one(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found in db",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Done!!"}
