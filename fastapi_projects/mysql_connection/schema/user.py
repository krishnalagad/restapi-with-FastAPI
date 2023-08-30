from pydantic import BaseModel

class UserShowSchema(BaseModel):
    name: str
    email: str
    
    class Config:
        orm_mode: True
        
class UserCreateSchema(UserShowSchema):
    password: str