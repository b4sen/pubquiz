from fastapi import APIRouter

from .admin import router as admin_router

api_router = APIRouter(prefix="/api")
api_router.include_router(admin_router)
