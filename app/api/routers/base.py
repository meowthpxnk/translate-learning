from app.api.configuration.metadata import TagsMetadata
from app.api.routers.__base import Router, base_responses
from app.api.schemas import BaseDBObject, BaseDBObjectForm
from app.database.models import BaseModel
from app.root import db


router = Router(tag=TagsMetadata.Base)


@router.get(
    "/object",
    responses={
        **base_responses,
        200: {"model": list[BaseDBObject]},
    },
)
async def get_objects():
    """Base doc for route"""
    return BaseModel.get_all()


@router.post(
    "/object",
    responses={
        **base_responses,
    },
)
async def create_object(form: BaseDBObjectForm):
    """Base doc for route"""
    obj = BaseModel(data=form.data)
    db.session.add(obj)
    db.session.commit()


@router.get(
    "/object/{id}",
    responses={
        **base_responses,
        200: {"model": BaseDBObject},
    },
)
async def get_single_object(id: int):
    """Base doc for route"""
    return BaseModel.find_by(BaseModel.id, id)


@router.put(
    "/object/{id}",
    responses={
        **base_responses,
    },
)
async def change_object(id: int, data: BaseDBObjectForm):
    """Base doc for route"""
    obj = BaseModel.find_by(BaseModel.id, id)
    obj.data = data.data
    db.session.commit()


@router.delete(
    "/object/{id}",
    responses={
        **base_responses,
    },
)
async def delete_object(id: int):
    """Base doc for route"""
    obj = BaseModel.find_by(BaseModel.id, id)
    db.session.delete(obj)
    db.session.commit()
