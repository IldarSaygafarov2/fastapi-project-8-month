from typing import Annotated
from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_jwt_service, get_password_service, get_repo

from infrastructure.database.repo.requests import RequestsRepo


router = APIRouter(
    prefix=config.api_prefix.v1.auth,
    tags=["Auth"],
)


@router.post("/register")
async def register_user():
    pass


@router.post("/login")
async def login_user():
    pass
