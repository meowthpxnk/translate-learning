import logging

from fastapi.requests import Request
from fastapi.responses import JSONResponse
from uvicorn.protocols.utils import get_client_addr, get_path_with_query_string

from . import api


logger = logging.getLogger()


@api.exception_handler(Exception)
async def default_exc_handler(request: Request, exc):
    scope = request.scope
    error = str(exc)
    addr = get_client_addr(scope)
    path = get_path_with_query_string(scope)
    method = scope["method"]
    version = scope["http_version"]
    logger.error(f'{addr} - "{method} {path} {version}", reason: {error}')
    return JSONResponse({"error": error}, status_code=400)
