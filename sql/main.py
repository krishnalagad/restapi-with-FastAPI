from fastapi import FastAPI
from sql.routes import user

app = FastAPI()

app.include_router(user.router)