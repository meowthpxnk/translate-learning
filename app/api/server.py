from uvicorn import Config, Server

from app.root import settings

from . import api


config = Config(
    app=api,
    host=settings.api.host,
    port=settings.api.port,
    log_config=None,
)

server = Server(config)
