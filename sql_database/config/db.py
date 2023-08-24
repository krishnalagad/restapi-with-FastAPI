import databases
import sqlalchemy

DATABASE_URL = "mysql+mysqlconnector://root:krishna24@localhost:3306/revise"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
