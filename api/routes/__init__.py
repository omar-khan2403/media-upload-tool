from fastapi import APIRouter
from routes.map import router as map_router
from routes.auth import router as auth_router


router = APIRouter()

router.include_router(map_router, prefix="/map", tags=["map"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])