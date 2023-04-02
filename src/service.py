from typing import Any, Type

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


class BaseRepo:
    def __init__(self, model: Type[SQLModel], fk_fields: dict | None = None):
        self.model = model
        self.fk_fields = fk_fields

    async def list(self, session: AsyncSession, filters) -> list[SQLModel]:
        result = await session.execute(select(self.model).filter_by(**filters).order_by("id"))
        return result.scalars().all()

    async def retrieve(self, session: AsyncSession, object_id: int) -> SQLModel:
        result = await session.get(self.model, object_id)
        if not result:
            raise HTTPException(status_code=404, detail="Object not found")
        return result

    async def _fk_check(self, session: AsyncSession, key: str, value: Any) -> None:
        if key in self.fk_fields:
            model = self.fk_fields[key]
            if not await session.get(model, value):
                raise HTTPException(status_code=400, detail=f"Foreign Key {key}={value} does not exist")

    async def partial_update(self, session: AsyncSession, object_id: int, body: SQLModel) -> SQLModel:
        db_object = await self.retrieve(session, object_id)
        data = body.dict(exclude_unset=True)
        for key, value in data.items():
            if self.fk_fields:
                await self._fk_check(session, key, value)
            setattr(db_object, key, value)
        await session.commit()
        return db_object

    async def create(self, session: AsyncSession, body: SQLModel) -> SQLModel:
        data = body.dict(exclude_unset=True)
        for key, value in data.items():
            if self.fk_fields:
                await self._fk_check(session, key, value)
        db_object = self.model.from_orm(body)
        session.add(db_object)
        await session.commit()
        return db_object
