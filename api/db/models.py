from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from database import Base


class User(Base):
    __tablename__ = "users"

    u_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

class Map(Base):
    __tablename__ = "maps"

    map_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=False)
    filename = Column(String, nullable=False)
    storage_name = Column(String, nullable=False)
    filetype = Column(String, index=False)
    size = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.u_id"), nullable=True)
    upload_dt = Column(DateTime, nullable=False)

