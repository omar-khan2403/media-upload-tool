from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)



class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String, index=True)
    extension = Column(String, index=true)
    size = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))
    upload_dt = Column(TIMESTAMP)

