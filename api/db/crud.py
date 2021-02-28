from sqlalchemy.orm import Session

import models, schema


def get_media_one(db: Session, media_id: int):
    '''get one media metadata for display'''
    return db.query(models.Media).filter(models.Media.id == media_id).first()


def get_media(db: Session, skip: int = 0, limit: int = 100):
    '''get all the media displayed for a user'''
    return db.query(models.Media).offset(skip).limit(limit).all()


def create_media(db: session, media: schema.Media):

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


def delete_media(db: Session, media_id: int):
    '''delete a media file'''

    return 'Media Deleted'
