from pydantic import BaseModel, Field
from app.breed.shemas import BreedBase


class KittenBase(BaseModel):
    name: str = Field(
        ...,
        title="Kitten Name",
        description="The name of the kitten.",
        example="Vasya",
        max_length=50,
    )
    color: str = Field(
        ...,
        title="Kitten Color",
        description="The color of the kitten.",
        example="Black",
        max_length=30,
    )
    age: int = Field(
        ...,
        title="Kitten Age",
        description="The age of the kitten in months.",
        example=2,
        ge=0,
    )
    description: str = Field(
        default="",
        title="Kitten Description",
        description="A brief description of the kitten.",
        max_length=250,
    )



class KittenCreate(KittenBase):
    breed_id: int = Field(
        ...,
        title="Breed ID",
        description="The ID of the breed the kitten belongs to.",
        example=1,
    )


class KittenID:
    id: int = Field(
        ...,
        title="Kitten ID",
        description="The unique identifier for the kitten.",
        example=10,
    )


class SKitten(KittenBase, KittenID):
    breed: BreedBase = Field(..., title="Breed", description="The breed of the kitten.")

    class Config:
        from_attributes = True
