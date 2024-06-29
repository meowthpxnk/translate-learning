from app.api.configuration.metadata import TagsMetadata
from app.api.routers.__base import Router, base_responses
from app.api.schemas import UserForm, UserSchema, WordForm, WordSchema
from app.database.models import Dictionary, User, Word
from app.root import db
from app.utilities.password import check_password, hash_password


router = Router(tag=TagsMetadata.Dictionary, prefix="/dictionary")

ADMIN_USERNAME = "meowthpxnk"


@router.post(
    "/word",
    responses={
        **base_responses,
        200: {"model": WordSchema},
    },
)
async def set_word(data: WordForm):
    """Base doc for route"""
    user = User.find_by(User.username, ADMIN_USERNAME)
    word = Word()
    word.word = data.word
    word.translate = data.translate

    if user.dictionary is None:
        user.dictionary = Dictionary()
        db.session.commit()

    user.dictionary.words.append(word)
    db.session.commit()

    return WordSchema(
        word=word.word,
        translate=word.translate,
        id=word.id,
    )


@router.delete(
    "/word/{id}",
    responses={
        **base_responses,
    },
)
async def remove_word(id):
    """Base doc for route"""
    word = Word.find_by(Word.id, id)
    db.session.delete(word)
    db.session.commit()
    return


@router.get(
    "",
    responses={
        **base_responses,
        200: {"model": list[WordSchema]},
    },
)
async def get_dictionary():
    """Base doc for route"""
    user = User.find_by(User.username, ADMIN_USERNAME)
    return [
        WordSchema(
            id=word.id,
            word=word.word,
            translate=word.translate,
        )
        for word in user.dictionary.words
    ]
