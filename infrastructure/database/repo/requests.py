from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from .user import UserRepo


@dataclass
class RequestsRepo:
    session: AsyncSession

    @property
    def user(self) -> UserRepo:
        return UserRepo(self.session)