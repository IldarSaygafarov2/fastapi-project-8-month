from backend.core.schemas.user import CreateUserDTO, UserDTO
from backend.core.services.password_service import PasswordService
from infrastructure.database.repo.requests import RequestsRepo


class RegisterUserInteractor:
    def __init__(self, repo: RequestsRepo, password_service: PasswordService):
        self.repo = repo
        self.password_service = password_service

    async def __call__(self, create_user: CreateUserDTO) -> UserDTO:
        existing_user = await self.repo.user.is_user_exists(username=create_user.username)
        if existing_user:
            raise ValueError("user with this username already exists")
        hashed_password = self.password_service.hash_password(password=create_user.password)
        user = await self.repo.user.add_user(username=create_user.username, hashed_password=hashed_password)
        return UserDTO.model_validate(user, from_attributes=True)
