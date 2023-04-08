from sqlmodel import Field, Relationship, SQLModel


class BookGenre(SQLModel, table=True):
    book_id: int | None = Field(default=None, foreign_key="book.id", primary_key=True)
    genre_id: int | None = Field(default=None, foreign_key="genre.id", primary_key=True)


class BookAuthor(SQLModel, table=True):
    book_id: int | None = Field(default=None, foreign_key="book.id", primary_key=True)
    author_id: int | None = Field(default=None, foreign_key="author.id", primary_key=True)


class BookBase(SQLModel):
    title: str
    writing_year: int

    def __str__(self):
        return self.title


class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    genres: list["Genre"] = Relationship(back_populates="books", link_model=BookGenre)
    authors: list["Author"] = Relationship(back_populates="books", link_model=BookAuthor)
    publishers: list["PublishBook"] = Relationship(back_populates="book")
