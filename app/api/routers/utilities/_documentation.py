from fastapi.responses import HTMLResponse

from app.api.routers.__base import Router
from app.utilities.path import read_static_file


router = Router(include_in_schema=False)


@router.get("/docs")
def documentation():
    html = read_static_file("Docs.html")

    return HTMLResponse(html)
