from fastapi import FastAPI

from .configuration import config, tags_metadata

api = FastAPI(
    docs_url=None,
    openapi_tags=tags_metadata,
    **config,
)

from app.root import logger

from MeowthLogger.utilities.fastapi.views import get_log_stream_views_router

api.include_router(get_log_stream_views_router(logger))

from . import handlers, middlewares, routers
