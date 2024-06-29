from pydantic import BaseModel


class BaseDBObject(BaseModel):
    id: int
    data: str


class BaseDBObjectForm(BaseModel):
    data: str


class ErrorReason(BaseModel):
    error: str
