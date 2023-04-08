import datetime

from sqlmodel import Field, Relationship, SQLModel

from src.library.models.book import BookAuthor, BookGenre
from src.library.models.country import Country


class AuthorBase(SQLModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    patronymic: str | None = None
    birthday: datetime.date | None = None
    day_of_death: datetime.date | None = None
    biography: str | None = None

    country_id: int | None = Field(default=None, foreign_key="country.id")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    country: Country | None = Relationship(back_populates="authors")
    books: list["Book"] = Relationship(back_populates="authors", link_model=BookAuthor)


class AuthorRead(AuthorBase):
    id: int


class AuthorUpdate(AuthorBase):
    first_name: str | None = None
    last_name: str | None = None
    country_id: int | None = None


class AuthorCreate(AuthorBase):
    pass


class AuthorWithCountry(AuthorRead):
    country: Country | None = None
