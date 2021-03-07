from fastapi import APIRouter
from routes.map import router as map_router


router = APIRouter()

router.include_router(map_router, prefix="/map", tags=["map"])