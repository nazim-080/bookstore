from fastapi import FastAPI

from src.authors.router import author_router
from src.db import run_async_upgrade

app = FastAPI(title="Bookstore", debug=True)


@app.on_event("startup")
async def startup() -> None:
    """Startup application."""

    await run_async_upgrade()

app.include_router(author_router)
