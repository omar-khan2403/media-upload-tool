from fastapi import APIRouter
from routes.media import router as media_router


router = APIRouter()

router.include_router(media_router, prefix="/map", tags=["map"])