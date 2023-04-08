from fastapi import FastAPI
from sqladmin import Admin

from src.db import engine, run_async_upgrade
from src.library.admin import AuthorAdmin, BookAdmin, CountryAdmin, GenreAdmin, PublishBookAdmin, PublisherAdmin
from src.library.router import book_router

app = FastAPI(title="Bookstore", debug=True)
admin = Admin(app, engine)

admin.add_view(AuthorAdmin)
admin.add_view(CountryAdmin)
admin.add_view(BookAdmin)
admin.add_view(GenreAdmin)
admin.add_view(PublisherAdmin)
admin.add_view(PublishBookAdmin)


@app.on_event("startup")
async def startup() -> None:
    """Startup application."""

    await run_async_upgrade()


app.include_router(book_router)
