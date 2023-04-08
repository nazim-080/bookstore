import datetime

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from starlette.requests import Request

from src.db import get_session
from src.library.models.author import Author, AuthorCreate, AuthorRead, AuthorUpdate, AuthorWithCountry
from src.library.models.country import Country, CountryCreate, CountryRead, CountryUpdate
from src.service import BaseRepo

book_router = APIRouter()

author_crud = BaseRepo(Author, {"country_id": Country})
country_crud = BaseRepo(Country)


@book_router.get("/author", response_model=list[AuthorRead])
async def get_authors(
    request: Request,
    session: AsyncSession = Depends(get_session),
    first_name: str | None = None,
    last_name: str | None = None,
    birthday: datetime.date = None,
    day_of_death: datetime.date | None = None,
):
    return await author_crud.list(session, request.query_params._dict)


@book_router.post("/author", response_model=AuthorRead)
async def create_author(body: AuthorCreate, session: AsyncSession = Depends(get_session)):
    return await author_crud.create(session, body)


@book_router.get("/author/{author_id}", response_model=AuthorWithCountry)
async def get_author(author_id: int, session: AsyncSession = Depends(get_session)):
    return await author_crud.retrieve(session, author_id)


@book_router.patch("/author/{author_id}", response_model=AuthorRead)
async def patch_author(author_id: int, body: AuthorUpdate, session: AsyncSession = Depends(get_session)):
    return await author_crud.partial_update(session, author_id, body)


@book_router.get("/country", response_model=list[CountryRead])
async def get_countries(
    request: Request,
    session: AsyncSession = Depends(get_session),
):
    return await country_crud.list(session, request.query_params._dict)


@book_router.post("/country", response_model=CountryRead)
async def create_country(body: CountryCreate, session: AsyncSession = Depends(get_session)):
    return await country_crud.create(session, body)


@book_router.get("/country/{country_id}", response_model=CountryRead)
async def get_country(country_id: int, session: AsyncSession = Depends(get_session)):
    return await country_crud.retrieve(session, country_id)


@book_router.patch("/country/{country_id}", response_model=CountryRead)
async def patch_country(country_id: int, body: CountryUpdate, session: AsyncSession = Depends(get_session)):
    return await country_crud.partial_update(session, country_id, body)
