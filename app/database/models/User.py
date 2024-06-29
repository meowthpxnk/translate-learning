import typing

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .__Base import Base


if typing.TYPE_CHECKING:
    from .Dictionary import Dictionary


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String)
    password_hash: Mapped[bytes] = mapped_column(String)

    dictionary: Mapped["Dictionary"] = relationship(back_populates="user")
