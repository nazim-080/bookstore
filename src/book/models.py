import datetime

from sqlmodel import Field, Relationship, SQLModel


class CountryBase(SQLModel):
    name: str


class Country(CountryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    authors: list["Author"] = Relationship(back_populates="country", sa_relationship_kwargs={"lazy": "selectin"})


class CountryRead(CountryBase):
    id: int


class CountryUpdate(CountryBase):
    pass


class CountryCreate(CountryBase):
    pass


class AuthorBase(SQLModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    patronymic: str | None = None
    birthday: datetime.date | None = None
    day_of_death: datetime.date | None = None
    biography: str | None = None

    country_id: int | None = Field(default=None, foreign_key="country.id")


class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    country: Country | None = Relationship(back_populates="authors")


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
