from ninja import NinjaAPI
from core.api.endpoints.router import api_router

api_app = NinjaAPI(
    title='HD Realty API',
    version='1.0.0',
)

api_app.add_router('/v1/', api_router)
