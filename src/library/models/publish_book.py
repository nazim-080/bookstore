from sqlmodel import Field, Relationship, SQLModel


class PublishBookBase(SQLModel):
    book_id: int | None = Field(default=None, foreign_key="book.id")
    publisher_id: int | None = Field(default=None, foreign_key="publisher.id")
    publication_year: int | None = None
    page_count: int | None
    description: str | None = None


class PublishBook(PublishBookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    book: "Book" = Relationship(back_populates="publishers")
    publisher: "Publisher" = Relationship(back_populates="published_books")

    def __str__(self):
        return f"{self.book} - {self.publisher}"
