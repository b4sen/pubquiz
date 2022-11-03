from fastapi import APIRouter

from .quiz import router as quiz_router

router = APIRouter(prefix="/admin")
router.include_router(quiz_router)
