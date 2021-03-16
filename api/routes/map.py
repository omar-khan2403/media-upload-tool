from typing import List
import uuid
import os
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
async def get_maps(skip: int= 0, limit: int=100, db: Session = Depends(get_db)):
    '''returns a list of existing media'''
    media = crud.get_maps(db, skip, limit)

    return media


@router.post("/")
async def upload_map(file: UploadFile = File(...), name: str = Form(None), db: Session = Depends(get_db)):
    '''uploads media metadata to DB and file to minIO container'''

    map_file = file.file

    #checked = maps.check_csv(map_file)
    #if checked is False:
    #    raise HTTPException(status_code=400, detail="Invalid File Metadata.")

    filename = file.filename
    filetype = file.content_type
    print(filename)
    size = len(map_file.read())
    print(size)

    map_file.seek(0)

    storage_name = str(uuid.uuid4()) + '.' + filename.split('.')[-1]
    upload_response = minio_media.upload_file(storage_name, bucket, map_file)

    if upload_response is False:
        raise HTTPException(status_code=400, detail="Error Uploading File.")

    map_dict = {
        'name': name,
        'filename': filename,
        'storage_name': storage_name,
        'upload_dt': datetime.utcnow(),
        'filetype': filetype,
        'size': size,
    }

    map_schema = schema.MapIn(**map_dict)
    print(map_schema)

    db_media = crud.create_map(db, map_schema)

    return {"detail": "Map data uploaded."}


@router.get("/{map_id}")
async def get_one(map_id: int, db: Session = Depends(get_db)):
    '''gets a specific media file'''
    map = crud.get_map_one(db, map_id)

    # if meta is not a link, get presigned url 
    url = minio_media.create_presigned_url(bucket, map.storage_name)

    print(url)

    return map

@router.delete("/{media_id}")
async def delete_one(media_id: int, db: Session = Depends(get_db)):
    '''deletes a specific media file and metadata'''
    response = crud.delete_one(db, media_id)

    return response
