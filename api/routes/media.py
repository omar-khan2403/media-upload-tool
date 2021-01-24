from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_media():
    '''returns a list of existing media'''

    return


@router.post("/")
def upload_media():
    '''uploads media metadata to DB and file to minIO container'''
    return
