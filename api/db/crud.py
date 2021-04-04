from sqlalchemy.orm import Session

import db.models as models
import db.schema as schema

def get_map_one(db: Session, map_id: int):
    '''get one map metadata for display'''
    return db.query(models.Map).filter(models.Map.map_id == map_id).first()


def get_maps(db: Session, skip: int = 0, limit: int = 100):
    '''get all the maps displayed for a user'''
    return db.query(models.Map).offset(skip).limit(limit).all()


def get_user_maps(db: Session, user_id: int,skip: int = 0, limit: int = 100):
    '''get all maps a user has uploaded'''
    return db.query(models.Map).filter(models.Map.owner_id == user_id).offset(skip).limit(limit).all()


def create_map(db: Session, media: schema.Map):
    '''Add a map'''

    db_media = models.Map(
        name=media.name,
        filename=media.filename,
        filetype=media.filetype, 
        storage_name=media.storage_name,
        size=media.size,
        owner_id=media.owner_id,
        upload_dt=media.upload_dt
    )

    db.add(db_media)
    db.commit()
    db.refresh(db_media)

    return db_media


def delete_map(db: Session, map_id: int):
    '''delete a map meta'''

    return 'Media Deleted'


def get_user_one(db: Session, email: str):
    '''get a user by email to check they exist from google log in'''
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schema.User):
    '''Add a user'''

    db_user = models.User(
        name = user.name,
        email = user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
