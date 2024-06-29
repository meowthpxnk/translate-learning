from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.root import settings

engine = create_engine(settings.db.uri, pool_pre_ping=True)


class Session(Session):
    def commit(self, *args, **kwargs):
        try:
            super().commit(*args, **kwargs)
        except:
            self.rollback()
            raise


session = Session(engine, autoflush=False)

from .models.__Base import Base

# Base.metadata.create_all(engine)
