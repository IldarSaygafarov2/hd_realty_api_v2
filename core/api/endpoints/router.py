from ninja import Router

from .v1 import categories, main

api_router = Router()

api_router.add_router(prefix="/categories/", router=categories.router)
api_router.add_router(prefix="/main/", router=main.router)
