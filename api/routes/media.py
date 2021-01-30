from typing import List
from fastapi import APIRouter, Depends, File, UploadFile
from pydantic import BaseModel
from fastapi_pagination import Page, PaginationParams
from fastapi_pagination.ext.databases import paginate
import api.media.minio_media as minio_media

router = APIRouter()

@router.get("/")
def get_media():
    '''returns a list of existing media'''

    return


@router.post("/")
def upload_media(files: List[UploadFile] = File(...)):
    '''uploads media metadata to DB and file to minIO container'''
    
    for file in files:
        name = file.filename
        print(name)
        size = len(file)
        print(size)

    return


@router.get("/{media_id}")
def get_one(media_id: int):
    '''gets a specific media file'''

    return
