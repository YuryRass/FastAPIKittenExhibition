from fastapi import APIRouter

from app.breed.dao import BreedDAO
from app.breed.shemas import BreedBase

router: APIRouter = APIRouter(tags=["Породы котят"])


@router.get("/breeds/", summary="Список всех пород")
async def get_breeds() -> list[BreedBase]:
    """Возвращает список всех имеющихся пород котят."""
    return await BreedDAO.find()
