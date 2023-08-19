from fastapi import FastAPI
import models, schemas
from schemas import Blog
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post("/")
def index(request: Blog):
    return request
