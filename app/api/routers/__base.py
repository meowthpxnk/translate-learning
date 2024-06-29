from fastapi import APIRouter

from ..schemas import ErrorReason


class Router(APIRouter):
    def __init__(self, *args, tag=None, **kwargs):
        if tag:
            tag = str(tag)
        super().__init__(*args, tags=[tag], **kwargs)


base_responses = {400: {"model": ErrorReason}}
