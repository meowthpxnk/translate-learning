from pydantic import BaseModel


class Config(BaseModel):
    title: str
    description: str
    version: str = "0.0.1"


description = """
Base description for API
"""

config = Config(
    title="Base title for API",
    description=description,
)
config = config.model_dump()
