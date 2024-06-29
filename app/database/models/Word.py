import typing

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .__Base import Base


if typing.TYPE_CHECKING:
    from .Dictionary import Dictionary


class Word(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String)
    translate: Mapped[str] = mapped_column(String)

    dictionary_id: Mapped[int] = mapped_column(ForeignKey("dictionary.id"))
    dictionary: Mapped["Dictionary"] = relationship(back_populates="words")
