from fastapi import FastAPI

from schemas import Blog

app = FastAPI()


@app.post("/")
def index(request: Blog):
    return request
