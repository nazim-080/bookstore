from sqlmodel import Field, Relationship, SQLModel

from src.library.models.book import BookGenre


class GenreBase(SQLModel):
    name: str
    description: str | None = None

    def __str__(self):
        return self.name


class Genre(GenreBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    books: list["Book"] = Relationship(back_populates="genres", link_model=BookGenre)


class GenreRead(GenreBase):
    id: int


class GenreUpdate(GenreBase):
    pass


class GenreCreate(GenreBase):
    pass
