import asyncio
import json
from typing import Any, Generator

import pytest
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.breed.model import Breed
from app.config import get_settings
from app.database import Base, async_engine, async_session

settings = get_settings()


@pytest.fixture(scope='session')
def event_loop(request) -> Generator:
    """
    Создает экземпляр стандартного цикла событий
    для каждого тестового случая.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def prepare_database() -> None:
    """Создание тестовой базы данных"""
    assert settings.MODE == 'TEST'

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str) -> Any:
        with open(f"tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    breeds = open_mock_json("breed")
    session: AsyncSession
    async with async_session() as session:
        query = insert(Breed).values(breeds)
        await session.execute(query)
        await session.commit()