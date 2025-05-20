from sqlalchemy import exists, insert, select, update, func

from infrastructure.database.models import User
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def is_user_exists(self, username: str):
        query = select(exists().where(User.username == username))
        result = await self.session.execute(query)
        return result.scalar()

    async def add_user(self, username: str, hashed_password: str):
        insert_stmt = (
            insert(User)
            .values(
                username=username,
                hashed_password=hashed_password,
            )
            .returning(User)
        )
        result = await self.session.execute(insert_stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_by_username(self, username: str):
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
