from .. import api


from .utilities._documentation import router

api.include_router(router)


from .utilities._static import router

api.include_router(router)


from .user import router

api.include_router(router)

from .dictionary import router

api.include_router(router)
