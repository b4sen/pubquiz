from fastapi import APIRouter

from .quiz import router as quiz_router
from .question import router as question_router


router = APIRouter(prefix="/admin")
router.include_router(quiz_router)
router.include_router(question_router)
