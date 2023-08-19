# restapi-with-FastAPI

#### FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. In this repository I've created API's for SQLite database CRUD operation using FastAPI. 
#### I have used SQLAlchemy ORM to deal with database tables. Project contains usage of Http Responses according to their Http request type.

## Steps to start with FastAPI.
#### 1. Install Virtuale Environment
```
pip install virtualenv
```

#### 2. Create Virtual Environment for project.
##### Locate the directory of your project in your terminal and below mentioned command.
```
virtualenv venv
```

#### 3. Activate virtual environment
```
For Windows:  1) cd venv/scripts
              2) activate
              
For Linux:    source venv/bin/activate
```

#### 4. Install required packages.
```
cd ..
pip install -r requirements.txt
```

#### 5. Create main python file. e.g. index.py, main.py etc

#### 6. Run the app
```
uvicorn index:app --reload
```

#### 7. To deactivate virtual environment use this command:
```
deactivate
```
