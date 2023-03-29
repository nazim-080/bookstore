import datetime

from sqlmodel import SQLModel, Field


class AuthorBase(SQLModel):
    first_name: str
    last_name: str
    birthday: datetime.date | None = None
    day_of_death: datetime.date | None = None
    biography: str | None = None


class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class AuthorRead(AuthorBase):
    id: int


class AuthorPatch(AuthorBase):
    first_name: str | None = None
    last_name: str | None = None


class AuthorCreate(AuthorBase):
    pass
