from fastapi import APIRouter, Depends

from pubquiz.dependencies.auth import get_current_user

router = APIRouter(prefix="/member", dependencies=[Depends(get_current_user)])


@router.get("/")
def hello_member():
    return "Hello Member"
