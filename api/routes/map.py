from typing import List
from fastapi import APIRouter, Depends, File, UploadFile
from pydantic import BaseModel
from sqlalchemy.orm import Session
import media.minio_media as minio_media

from db import models, schema, crud
from database import SessionLocal

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
def upload_map(files: List[UploadFile] = File(...)):
    '''uploads media metadata to DB and file to minIO container'''
    
    for file in files:
        name = file.filename
        print(name)
        size = len(file)
        print(size)

    # check if file type is xls/xlsx/or csv




    return


@router.get("/{media_id}")
def get_one(media_id: int, db: Session = Depends(get_db)):
    '''gets a specific media file'''
    media = crud.get_media_one(db, media_id)

    # if meta is not a link, get presigned url 
    url = minio_media.create_presigned_url()

    return media

@router.delete("/{media_id}")
def delete_one(media_id: int, db: Session = Depends(get_db)):
    '''deletes a specific media file and metadata'''
    response = crud.delete_one(db, media_id)

    return response
