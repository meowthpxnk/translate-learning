from app.api.configuration.metadata import TagsMetadata
from app.api.routers.__base import Router, base_responses
from app.api.schemas import UserForm, UserSchema
from app.database.models import User
from app.root import db
from app.utilities.password import check_password, hash_password


router = Router(tag=TagsMetadata.User, prefix="/user")


@router.post(
    "/registrate",
    responses={
        **base_responses,
        200: {"model": UserForm},
    },
)
async def registrate_user(form: UserForm):
    """Base doc for route"""
    user = User()
    db.session.add(user)
    user.username = form.username

    password_hash = hash_password(form.password)
    user.password_hash = password_hash

    db.session.commit()

    return UserSchema(username=user.username)


@router.post(
    "/authorisate",
    responses={
        **base_responses,
        200: {"model": UserForm},
    },
)
async def authorisate_user(form: UserForm):
    """Base doc for route"""
    user = User.find_by(User.username, form.username)
    check_password(form.password, user.password_hash)
    return UserSchema(username=user.username)
