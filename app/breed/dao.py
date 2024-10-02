from app.base_dao import BaseDAO
from app.breed.model import Breed


class BreedDAO(BaseDAO):
    model = Breed
