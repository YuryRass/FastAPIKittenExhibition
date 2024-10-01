from fastapi import APIRouter, HTTPException

from app.kitten.dao import KittenDAO
from app.kitten.schemas import KittenCreate, SKitten


router: APIRouter = APIRouter(tags=["Котята"])


@router.get("/kittens/", response_model=list[SKitten])
async def get_kittens() -> list[SKitten]:
    return await KittenDAO.get_detailed()


@router.get("/kittens/breed/{breed_id}/", response_model=list[SKitten])
async def get_kittens_by_breed(breed_id: int) -> list[SKitten]:
    return await KittenDAO.get_detailed(breed_id=breed_id)


@router.get("/kittens/{kitten_id}/", response_model=SKitten)
async def get_kitten(kitten_id: int) -> SKitten:
    kitten = await KittenDAO.get_detailed(id=kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten


@router.post("/kittens/", response_model=SKitten)
async def create_kitten(kitten: KittenCreate) -> SKitten:
    res = await KittenDAO.add(**kitten.model_dump())
    return await KittenDAO.get_detailed(id=res.id)


@router.put("/kittens/{kitten_id}/", response_model=SKitten)
async def update_kitten(
    kitten_id: int,
    kitten: KittenCreate,
) -> SKitten:
    db_kitten = await KittenDAO.find_one_or_none(id=kitten_id)
    if db_kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")

    res = await KittenDAO.update(db_kitten.id, **kitten.model_dump())
    return await KittenDAO.get_detailed(id=res.id)


@router.delete("/kittens/{kitten_id}/")
async def delete_kitten(kitten_id: int) -> None:
    db_kitten = await KittenDAO.find_one_or_none(id=kitten_id)
    if db_kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    await KittenDAO.delete_rec(id=db_kitten.id)
    return {"deleted": kitten_id}
