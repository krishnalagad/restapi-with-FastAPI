from config.db import Base
from sqlalchemy import Integer, Column, String

class Users(Base):
    __tablename__ = 'fastapi_users'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(50))
    email=Column(String(100), unique=True)
    password=Column(String(100))
    
class Roles(Base):
    __tablename__ = 'fastapi_roles'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(50), unique=True)