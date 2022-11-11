from Api.config.settings import Settings
from fastapi import APIRouter


defaultRoute = APIRouter()

@defaultRoute.get('/')
async def index():
    settings = Settings()
    return {'message': f'Hello,Welcome to the {settings.app_name}.'}
