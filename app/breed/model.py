from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.kitten.model import Kitten


class Breed(Base):
    """Породы котят."""

    name: Mapped[str] = mapped_column(unique=True, index=True)
    kittens: Mapped[list["Kitten"]] = relationship(back_populates="breed")
