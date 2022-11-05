from fastapi import APIRouter

router = APIRouter(prefix="/member")


@router.get("/")
def hello_member():
    return "Hello Member"
