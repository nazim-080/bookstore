import datetime

from fastapi import APIRouter, Depends

from sqlmodel.ext.asyncio.session import AsyncSession
from starlette.requests import Request

from src.authors.models import Author, AuthorRead, AuthorPatch, AuthorCreate
from src.db import get_session
from src.service import BaseCRUD

author_router = APIRouter(tags=["author"], prefix="/authors")

author_crud = BaseCRUD(Author)


@author_router.get("/", response_model=list[AuthorRead])
async def get_authors(request: Request,
                      session: AsyncSession = Depends(get_session),
                      first_name: str | None = None,
                      last_name: str | None = None,
                      birthday: datetime.date = None,
                      day_of_death: datetime.date | None = None):
    return await author_crud.list(session, request.query_params._dict)


@author_router.post("/", response_model=AuthorRead)
async def create_author(body: AuthorCreate, session: AsyncSession = Depends(get_session)):
    return await author_crud.create(session, body)


@author_router.get("/{author_id}", response_model=AuthorRead)
async def get_author(author_id: int, session: AsyncSession = Depends(get_session)):
    return await author_crud.retrieve(session, author_id)


@author_router.patch("/{author_id}", response_model=AuthorRead)
async def patch_author(author_id: int, body: AuthorPatch, session: AsyncSession = Depends(get_session)):
    return await author_crud.partial_update(session, author_id, body)
