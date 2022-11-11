from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from Api.Routes.usersRoutes import userRoutes
from Api.Routes.defaultRoute import defaultRoute

app = FastAPI(title="FastAPI-Users-Backend",description = "CRUD API")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(userRoutes,tags=['Users'], prefix='/api/users')
app.include_router(defaultRoute)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


