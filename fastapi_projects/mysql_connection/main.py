from fastapi import FastAPI
from config.db import Base, SessionLocale, engine
from models.model import Users
from routes import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)

