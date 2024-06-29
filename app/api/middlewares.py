from fastapi.middleware.cors import CORSMiddleware

from . import api


api.add_middleware(CORSMiddleware, allow_origins=["*"])
