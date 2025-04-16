from pydantic import BaseModel

class Item(BaseModel): # Needs to inherit from BaseModel
    name: int # Name needs to be a string
    description: str

class User(BaseModel):
    username: str
    bio: str
    
    # You can raise your hands and give the answer to the chocolate question