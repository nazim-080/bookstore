from pydantic import HttpUrl
from sqlmodel import Field, Relationship, SQLModel

from src.library.models.country import Country


class PublisherBase(SQLModel):
    name: str
    isbn: str
    year_of_foundation: int
    site_url: HttpUrl | None = None
    description: str | None = None

    country_id: int | None = Field(default=None, foreign_key="country.id")

    def __str__(self):
        return self.name


class Publisher(PublisherBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    country: Country | None = Relationship(back_populates="publishers")
    published_books: list["PublishBook"] = Relationship(back_populates="publisher")
