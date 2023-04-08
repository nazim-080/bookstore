from sqladmin import ModelView

from src.library.models.author import Author
from src.library.models.book import Book
from src.library.models.country import Country
from src.library.models.genre import Genre
from src.library.models.publish_book import PublishBook
from src.library.models.publisher import Publisher


class AuthorAdmin(ModelView, model=Author):
    column_list = [
        Author.id,
        Author.first_name,
        Author.last_name,
        Author.middle_name,
        Author.patronymic,
        Author.biography,
        Author.birthday,
        Author.day_of_death,
        Author.country,
        Author.books,
    ]


class CountryAdmin(ModelView, model=Country):
    column_list = [Country.id, Country.name]


class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.title, Book.writing_year, Book.genres, Book.authors, Book.publishers]


class GenreAdmin(ModelView, model=Genre):
    column_list = [Genre.id, Genre.name]


class PublisherAdmin(ModelView, model=Publisher):
    column_list = [
        Publisher.id,
        Publisher.name,
        Publisher.isbn,
        Publisher.published_books,
        Publisher.country,
        Publisher.description,
        Publisher.site_url,
        Publisher.year_of_foundation,
    ]


class PublishBookAdmin(ModelView, model=PublishBook):
    column_list = [
        PublishBook.book,
        PublishBook.publisher,
        PublishBook.description,
        PublishBook.page_count,
        PublishBook.publication_year,
    ]
