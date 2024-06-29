import os

from fastapi.responses import FileResponse

from app.api.routers.__base import Router


router = Router(include_in_schema=False)


@router.get("/static/favicon.png", include_in_schema=False)
def favicon():
    return FileResponse(
        os.path.join(os.path.abspath("."), "static", "favicon.png")
    )
