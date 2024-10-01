from pydantic import BaseModel, Field


class BreedBase(BaseModel):
    name: str = Field(
        ...,
        title="Breed Name",
        description="The name of the breed.",
        example="Siamese",
        max_length=50,
    )


class BreedCreate(BreedBase):
    pass
