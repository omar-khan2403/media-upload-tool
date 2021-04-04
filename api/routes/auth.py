from typing import List
import uuid
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException, Request
from sqlalchemy.orm import Session

from db import models, schema, crud
from database import SessionLocal

from google.oauth2 import id_token
from google.auth.transport import requests

load_dotenv()

# google oauth client ID
CLIENT_ID = os.getenv('CLIENT_ID')

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/google")
async def google_auth(request: Request, db: Session = Depends(get_db)):

    request = await request.body()
    google_info = json.loads(request)['body']

    try:
        token = json.loads(google_info)['token']
    
    except:
        raise HTTPException(status_code=400, detail="No Token.")
    # verify google token
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        userid = idinfo['sub']
        
    except ValueError:
        # Invalid token
        raise HTTPException(status_code=400, detail="Token Invalid.")
    
    # if user does not exist add to user tables and retrieve id
    user_info = json.loads(google_info)['user']
    name = user_info['name']
    email = user_info['email']

    user_check = crud.get_user_one(db, email)

    if user_check is None:
        user_dict = {
            'name': name,
            'email': email
        }

        user_schema = schema.UserIn(**user_dict)
        db_user = crud.create_user(db, user_schema)

    # if user does exist retrieve id
    else:
        db_user = user_check
    
    return {'u_id': db_user.u_id, 'u_name': db_user.name, 'u_email': db_user.email, 'is_auth': True}

@router.delete("/logout")
def logout():


    return
