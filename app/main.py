from fastapi import FastAPI

from app.routers.health_router import health_router


app = FastAPI()

app.include_router(health_router)
