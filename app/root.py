# import logging

from MeowthLogger import Logger
from MeowthLogger.utilities.fastapi.log_stream import StreamManager

from .loop import loop
from .settings import settings


stream_manager = StreamManager(loop)

logger = Logger(
    use_uvicorn=True,
    logger_level=settings.logger.level.value,
    stream=stream_manager,
)


from . import database as db


db


from .api.server import server


# logger = logging.getLogger()
loop.create_task(server.serve())
