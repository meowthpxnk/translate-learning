from sqlalchemy import select
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, InstrumentedAttribute


class Base(DeclarativeBase):
    __name__: str

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    def find_by(cls, by: InstrumentedAttribute, value):
        from .. import session

        exc = Exception(
            f"Not found {cls.__name__.lower()} with {by.name} {value}"
        )

        stmt = select(cls).where(by == value)

        try:
            object = session.scalars(stmt).first()

        except Exception:
            raise exc

        if not object:
            raise exc

        return object

    @classmethod
    def get_all(cls):
        from .. import session

        stmt = select(cls)
        return session.scalars(stmt).all()
