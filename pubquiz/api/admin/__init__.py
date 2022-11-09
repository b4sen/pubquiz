from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from pubquiz import schemas
from pubquiz.db.models import Admin
from pubquiz.dependencies import get_db
from pubquiz.dependencies.auth import (ACCESS_TOKEN_EXPIRE_MINUTES,
                                       authenticate_user, create_access_token,
                                       get_current_user, hash_password)

from .member import router as member_router
from .question import router as question_router
from .quiz import router as quiz_router
from .team import router as team_router

router = APIRouter(prefix="/admin")
router.include_router(quiz_router, tags=["admin quiz endpoints"])
router.include_router(question_router, tags=["admin question endpoints"])
router.include_router(team_router, tags=["admin team endpoints"])
router.include_router(member_router, tags=["admin member endpoints"])


@router.post(
    "/register",
    dependencies=[Depends(get_current_user)],
    response_model=schemas.AdminResponse,
)
def register_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    data = {"username": admin.username, "password": hash_password(admin.password)}
    a = Admin(**data)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a


@router.post("/token")
def get_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
