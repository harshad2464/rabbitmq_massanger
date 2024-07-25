from fastapi import APIRouter
from app.api.endpoints import get_data
from app.api.endpoints import home

api_router = APIRouter()

api_router.include_router(get_data.router, prefix="/get_data", tags=["get data"])
api_router.include_router(home.router, prefix="/home", tags=["home"])
