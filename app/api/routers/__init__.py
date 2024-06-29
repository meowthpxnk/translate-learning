from .. import api


from .utilities._documentation import router

api.include_router(router)


from .utilities._static import router

api.include_router(router)


from .base import router

api.include_router(router)
