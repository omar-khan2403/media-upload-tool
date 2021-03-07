from sqlalchemy.orm import Session

import db.models as models
import db.schema as schema

def get_map_one(db: Session, media_id: int):
    '''get one map metadata for display'''
    return db.query(models.Media).filter(models.Media.id == media_id).first()


def get_maps(db: Session, skip: int = 0, limit: int = 100):
    '''get all the maps displayed for a user'''
    return db.query(models.Media).offset(skip).limit(limit).all()


def create_map(db: Session, media: schema.Media):

    db_media = models.Media(
        name=media.name, 
        type=media.type, 
        extension=media.extension,
        size=media.size,
        owner_id=media.owner_id
        )

    db.add(db_media)
    db.commit()
    db.refresh(db_media)

    return db_media


def delete_map(db: Session, media_id: int):
    '''delete a map meta'''

    return 'Media Deleted'
