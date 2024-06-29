from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .__Base import Base


class BaseModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(String)
