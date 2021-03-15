from typing import List
import uuid
from datetime import datetime
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import media.minio_media as minio_media
import media.maps as maps

from db import models, schema, crud
from database import SessionLocal

load_dotenv()

bucket = os.getenv('AWS_BUCKET')

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_maps(skip: int= 0, limit: int=100, db: Session = Depends(get_db)):
    '''returns a list of existing media'''
    media = crud.get_media(db, skip, limit)

    return media


@router.post("/")
def upload_map(file: UploadFile = File(...), name: str = Form(None), db: Session = Depends(get_db)):
    '''uploads media metadata to DB and file to minIO container'''

    map_file = file.file

    #checked = maps.check_excel(map_file)
    #if checked is False:
    #    raise HTTPException(status_code=400, detail="Invalid File Metadata.")

    filename = file.filename
    filetype = file.content_type
    print(filename)
    size = len(map_files.read())
    print(size)

    map_file.seek(0)

    storage_name = str(uuid.uuid4()) + '.' + name.split('.')[-1]
    upload_response = minio_media.upload_file(storage_name, bucket, file.read)

    if response is False:
        raise HTTPException(status_code=400, detail="Error Uploading File.")

    map_dict = {
        'name': name,
        'filename': filename,
        'storage_name': storage_name,
        'upload_dt': datetime.utcnow(),
        'type': filetype,
        'size': size,
    }

    print(map_dict)

    #db_media = crud.create_map(db, schema.Map(**map_dict))

    return {"detail": "Map data uploaded."}


@router.get("/{map_id}")
def get_one(media_id: int, db: Session = Depends(get_db)):
    '''gets a specific media file'''
    map = crud.get_media_one(db, map_id)

    # if meta is not a link, get presigned url 
    url = minio_media.create_presigned_url(bucket, media.storage_name)

    print(url)

    return media

@router.delete("/{media_id}")
def delete_one(media_id: int, db: Session = Depends(get_db)):
    '''deletes a specific media file and metadata'''
    response = crud.delete_one(db, media_id)

    return response
