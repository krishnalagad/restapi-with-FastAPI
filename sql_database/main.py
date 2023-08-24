from fastapi import FastAPI
from sql_database.config import db
from sql_database.schemas.userSchema import User
from sql_database.models.user import users
from sql_database.config.db import database


app = FastAPI(tags=["User"], prefix="/user")


@app.post("/")
async def create_user(user: User):
    query = users.insert().values(
        name=user.name, email=user.email, password=user.password
    )
    user_id = await database.execute(query)
    return {"user_id": user_id}
