from datetime import datetime
from pydantic import BaseModel



class AttindanceBase(BaseModel):
    name:str
    date: datetime
    class Config():
        orm_mode = True



