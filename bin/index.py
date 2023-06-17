from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bin.config import settings

from bin.routes.api.v0 import router as APIv0
from bin.routes.web.v0 import router as WEBv0

_app = FastAPI(title=settings.PROJECT_NAME)
_app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        str(origin)
        for origin in settings.BACKEND_CORS_ORIGINS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
_app.include_router(router=APIv0, prefix='/api/v0')
_app.include_router(router=WEBv0, prefix='')
