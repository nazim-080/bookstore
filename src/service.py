from typing import Type

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


class BaseCRUD:
    def __init__(self, model: Type[SQLModel]):
        self.model = model

    async def list(self, session: AsyncSession, filters):
        result = await session.execute(select(self.model).filter_by(**filters))
        return result.scalars().all()

    async def retrieve(self, session: AsyncSession, object_id: int):
        result = await session.get(self.model, object_id)
        if not result:
            raise HTTPException(status_code=404, detail="Object not found")
        return result

    async def partial_update(self, session: AsyncSession, object_id: int, body: SQLModel):
        db_object = await self.retrieve(session, object_id)
        data = body.dict(exclude_unset=True)
        for key, value in data.items():
            setattr(db_object, key, value)
        await session.commit()
        return db_object

    async def create(self, session: AsyncSession, body: SQLModel):
        db_object = self.model.from_orm(body)
        session.add(db_object)
        await session.commit()
        return db_object
