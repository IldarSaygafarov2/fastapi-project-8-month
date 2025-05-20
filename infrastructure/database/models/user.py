from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, created_at

from .mixins.int_id_pk import IntIdPxMixin


class User(Base, IntIdPxMixin):
    username: Mapped[str] = mapped_column(String(64))
    hashed_password: Mapped[str] = mapped_column(String(1024))
    registered_at: Mapped[created_at]
