from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class MapIn(BaseModel):
    name: str
    filename: str
    storage_name: str
    filetype: str
    size: int
    owner_id: Optional[int]
    upload_dt: datetime

    class Config:
        orm_mode: True

class Map(BaseModel):
    map_id: int
    name: str
    filename: str
    storage_name: str
    filetype: str
    size: int
    owner_id: Optional[int]
    upload_dt: datetime

    class Config:
        orm_mode: True


class UserIn(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode: True


class User(UserIn):
    u_id: int

    class Config:
        orm_mode: True
