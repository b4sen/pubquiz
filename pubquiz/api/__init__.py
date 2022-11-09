from fastapi import APIRouter

from .admin import router as admin_router
from .team import router as team_router
from .quiz import router as quiz_router

api_router = APIRouter(prefix="/api")
api_router.include_router(admin_router)
api_router.include_router(team_router, tags=["team endpoints"])
api_router.include_router(quiz_router)
