import models
from sqlalchemy.orm import Session


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs
