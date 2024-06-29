from pydantic import BaseModel


class Tag(BaseModel):
    name: str
    description: str

    def __str__(self):
        return self.name


class TagsMetadata:
    Base = Tag(
        name="Base",
        description="Base description for tag",
    )


tags: list[Tag] = [
    TagsMetadata.Base,
]

tags_metadata = [tag.model_dump() for tag in tags]
