from fastapi import FastAPI
from routers.uie import mod as uie
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3333",
    "http://localhost:4173"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(uie.router)

