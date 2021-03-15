from sqlalchemy.orm import Session

import db.models as models
import db.schema as schema

def get_map_one(db: Session, map_id: int):
    '''get one map metadata for display'''
    return db.query(models.Media).filter(models.Map.map_id == map_id).first()


def get_maps(db: Session, skip: int = 0, limit: int = 100):
    '''get all the maps displayed for a user'''
    return db.query(models.Map).offset(skip).limit(limit).all()


def create_map(db: Session, media: schema.Map):

    db_media = models.Map(
        name=media.name,
        filename=media.filename
        filetype=media.filetype, 
        size=media.size,
        owner_id=media.owner_id
        upload_dt=media.upload_dt
        )

    db.add(db_media)
    db.commit()
    db.refresh(db_media)

    return db_media


def delete_map(db: Session, map_id: int):
    '''delete a map meta'''

    return 'Media Deleted'
