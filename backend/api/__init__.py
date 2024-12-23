from fastapi import APIRouter
from backend.api.v1 import router as api_router_v1


from backend.app.config import config


router = APIRouter(prefix=config.api_prefix.prefix)

router.include_router(router=api_router_v1)
