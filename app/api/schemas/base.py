from pydantic import BaseModel


class ErrorReason(BaseModel):
    error: str


class UserSchema(BaseModel):
    username: str


class UserForm(BaseModel):
    username: str
    password: str


class WordForm(BaseModel):
    word: str
    translate: str


class WordSchema(BaseModel):
    id: int
    word: str
    translate: str
