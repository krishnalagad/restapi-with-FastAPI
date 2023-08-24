from sqlalchemy import Table, Column, Integer, String
from sql_database.config.db import metadata

users = Table(
    "fastapi_users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("email", String, unique=True, index=True),
    Column("password", String),
)
