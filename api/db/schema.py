from typing import List, Optional
from pydantic import BaseModel


class Media(BaseModel):
    id: int
    name: str
    storage_name: str
    type: str
    extension: str
    size: int
    owner_id: int

    class Config:
        orm_mode: True

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool

    class Config:
        orm_mode: True