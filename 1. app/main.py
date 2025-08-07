from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Store API com TDD")
app.include_router(router)
