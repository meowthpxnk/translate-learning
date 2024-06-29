# from fastapi import WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse

# from app.api.routers.__base import Router
# from app.utilities.path import read_static_file


# router = Router(include_in_schema=False)


# @router.get("/logs")
# async def get():
#     html = read_static_file("LogStreaming.html")
#     html = html.replace("{{ENV_TITLE}}", "Server log streamin")
#     return HTMLResponse(html)


# @router.websocket("/logs")
# async def log_stream(websocket: WebSocket):
#     from app.logger import logger

#     await logger.stream.connect(websocket)
#     try:
#         while True:
#             await websocket.receive_text()
#     except WebSocketDisconnect:
#         logger.stream.disconnect(websocket)
