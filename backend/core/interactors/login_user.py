from backend.core.schemas.user import LoginUserDTO
from backend.core.services.jwt_service import JwtService
from backend.core.services.password_service import PasswordService
from infrastructure.database.repo.requests import RequestsRepo


class LoginUserInteractor:
    def __init__(self, repo: RequestsRepo, password_service: PasswordService, jwt_service: JwtService):
        self.repo = repo
        self.password_service = password_service
        self.jwt_service = jwt_service

    async def __call__(self, login_user: LoginUserDTO) -> str:
        user = await self.repo.user.get_by_username(username=login_user.username)
        if not user or not self.password_service.verify_password(
                plain_password=login_user.password,
                hashed_password=user.hashed_password
        ):
            raise ValueError('invalid username or password')
        access_token = self.jwt_service.create_access_token({"sub": user.username})
        return access_token
