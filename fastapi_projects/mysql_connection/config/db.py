from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "mysql+pymysql://root:krishna24@127.0.0.1:3306/revise"

engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocale = sessionmaker(autocommit=False, bind=engine)

def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()