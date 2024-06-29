import typing

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .__Base import Base


if typing.TYPE_CHECKING:
    from .User import User
    from .Word import Word


class Dictionary(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="dictionary")

    words: Mapped[list["Word"]] = relationship(back_populates="dictionary")
