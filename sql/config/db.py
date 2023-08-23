from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:krishna24@localhost:3306/revise"

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()


# # create sqlalchemy engine
# engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# # create session factory
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# # database model
# Base = declarative_base()


# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()
