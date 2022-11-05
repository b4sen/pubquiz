from fastapi import APIRouter

from .member import router as member_router
from .question import router as question_router
from .quiz import router as quiz_router
from .team import router as team_router

router = APIRouter(prefix="/admin")
router.include_router(quiz_router)
router.include_router(question_router)
router.include_router(team_router)
router.include_router(member_router)
