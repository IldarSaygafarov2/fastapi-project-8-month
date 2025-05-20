from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from backend.app.config import config
from backend.app.dependencies import get_jwt_service, get_password_service, get_repo
from backend.core.schemas.user import UserDTO, LoginUserDTO, CreateUserDTO
from backend.core.services.password_service import PasswordService
from backend.core.services.jwt_service import JwtService


from infrastructure.database.repo.requests import RequestsRepo
from backend.core.interactors.register_user import RegisterUserInteractor
from backend.core.interactors.login_user import LoginUserInteractor


router = APIRouter(
    prefix=config.api_prefix.v1.auth,
    tags=["Auth"],
)


@router.post("/register", response_model=UserDTO)
async def register_user(
        user_register_data: CreateUserDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        password_service: Annotated[PasswordService, Depends(get_password_service)]
):
    interactor = RegisterUserInteractor(repo=repo, password_service=password_service)
    try:
        user = await interactor(create_user=user_register_data)
        return user
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)


@router.post("/login")
async def login_user(
        user_login_data: LoginUserDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        password_service: Annotated[PasswordService, Depends(get_password_service)],
        jwt_service: Annotated[JwtService, Depends(get_jwt_service)]
):
    interactor = LoginUserInteractor(repo=repo, password_service=password_service, jwt_service=jwt_service)
    try:
        token = await interactor(user_login_data)
        return {'access_token': token, "token_type": "bearer"}
    except ValueError as e:
        return JSONResponse(content={"UNAUTHORIZED": str(e)}, status_code=401)
