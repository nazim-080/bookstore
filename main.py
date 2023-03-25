from fastapi import FastAPI
from models.db import run_async_upgrade

app = FastAPI(title="Bookstore")


@app.on_event("startup")
async def startup() -> None:
    """Startup application."""

    await run_async_upgrade()


@app.get("/")
def hello():
    return "Hello World"
