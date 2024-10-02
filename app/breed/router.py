from fastapi import APIRouter

from app.breed.dao import BreedDAO
from app.breed.shemas import BreedBase, BreedCreate

router: APIRouter = APIRouter(tags=["Породы котят"])


@router.get("/breeds/", summary="Список всех пород", response_model=list[BreedBase])
async def get_breeds() -> list[BreedBase]:
    """Возвращает список всех имеющихся пород котят."""
    return await BreedDAO.find()


@router.post("/breeds/", summary="Добавление породы котят", response_model=BreedBase)
async def add_breed(breed: BreedCreate) -> BreedBase:
    """Добавление породы котят."""
    return await BreedDAO.add(**breed.model_dump())