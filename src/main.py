from fastapi import FastAPI
from routers.uie import mod as uie

app = FastAPI()

app.include_router(uie.router)