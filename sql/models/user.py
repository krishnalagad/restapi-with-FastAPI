from sql.config.db import meta
from sqlalchemy import Column, Integer, String, Table

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
)


# class User(Base):
#     __tablename__ = 'fastapi_users'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)
