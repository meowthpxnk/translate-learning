from pydantic import BaseModel


class Tag(BaseModel):
    name: str
    description: str

    def __str__(self):
        return self.name


class TagsMetadata:
    User = Tag(
        name="User",
        description="User functions",
    )

    Dictionary = Tag(
        name="Dictionary",
        description="Dictionary functions",
    )


tags: list[Tag] = [
    TagsMetadata.User,
    TagsMetadata.Dictionary,
]

tags_metadata = [tag.model_dump() for tag in tags]
