from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.base_dao import BaseDAO
from app.database import async_session
from app.kitten.model import Kitten


class KittenDAO(BaseDAO):
    model = Kitten

    @classmethod
    async def get_detailed(cls, **kwargs: Any) -> Any:
        """Подробный вывод информации о котятах."""
        session: AsyncSession
        async with async_session() as session:
            stmt = (
                select(cls.model)
                .options(joinedload(cls.model.breed))
                .filter_by(**kwargs)
            )
            result = await session.execute(stmt)
            if "id" in kwargs:
                return result.scalars().one_or_none()
            return result.scalars().all()
