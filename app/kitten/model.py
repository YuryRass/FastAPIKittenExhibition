from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.breed.model import Breed


class Kitten(Base):
    """Котята."""

    name: Mapped[str] = mapped_column(index=True)
    color: Mapped[str]
    age: Mapped[int]
    description: Mapped[str]
    breed_id = mapped_column(ForeignKey("breeds.id"))

    breed: Mapped["Breed"] = relationship(back_populates="kittens")
