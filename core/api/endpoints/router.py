from ninja import Router

from .v1 import categories


api_router = Router()

api_router.add_router(prefix='/categories/', router=categories.router)
