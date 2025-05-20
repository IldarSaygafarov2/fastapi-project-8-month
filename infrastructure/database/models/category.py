from datetime import datetime

from sqlalchemy import String

from .mixins.int_id_pk import IntIdPxMixin
from .base import Base, created_at, updated_at

from sqlalchemy.orm import Mapped, mapped_column


class Category(Base, IntIdPxMixin):
    name: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
