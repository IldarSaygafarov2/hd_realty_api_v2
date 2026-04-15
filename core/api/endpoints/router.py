from ninja import Router

from .v1 import advertisements, categories, districts, main

api_router = Router()

api_router.add_router(prefix="/main/", router=main.router)
api_router.add_router(prefix="/categories/", router=categories.router)
api_router.add_router(prefix="/districts/", router=districts.router)
api_router.add_router(prefix="/advertisements/", router=advertisements.router)
