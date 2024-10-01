from typing import Any

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session


class BaseDAO:
    """
    Основной DAO. Реализует основные CRUD-операции к модели
    """

    model = None

    @classmethod
    async def find_one_or_none(cls, **kwargs: Any) -> Any:
        """Осуществляет поиск записи."""
        session: AsyncSession
        async with async_session() as session:
            stmt = select(cls.model.__table__.columns).filter_by(**kwargs)
            result = await session.execute(stmt)
            return result.one_or_none()

    @classmethod
    async def find(cls, **kwargs: Any) -> Any:
        """Поиск всех записей из модели."""
        session: AsyncSession
        async with async_session() as session:
            stmt = select(cls.model.__table__.columns).filter_by(**kwargs)
            result = await session.execute(stmt)
            return result.all()

    @classmethod
    async def add(cls, **data: Any) -> Any:
        """Добавление записи в таблицу."""
        stmt = insert(cls.model).values(**data).returning(cls.model.__table__.columns)
        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
            return result.one()

    @classmethod
    async def update(cls, model_id: int, **data) -> Any:
        """Изменение записи в модели."""
        assert cls.model is not None
        stmt = (
            update(cls.model)
            .where(cls.model.id == model_id)
            .values(**data)
            .returning(cls.model.__table__.columns)
        )
        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
            return result.one()

    @classmethod
    async def delete_rec(cls, **kwargs: Any) -> None:
        """Удаление записей по условию."""
        stmt = delete(cls.model).filter_by(**kwargs)

        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
