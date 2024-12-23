from fastapi import APIRouter, Depends

from fastapi.security import HTTPBearer

from backend.app.config import config

from .routes.auth import router as auth_router


http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=config.api_prefix.v1.prefix,
    # dependencies=[Depends(http_bearer)],
)


router.include_router(router=auth_router)
