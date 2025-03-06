from services.base import BaseService
from models import Cargo

class CargoService(BaseService):
    def __init__(self, db):
        super().__init__(db, Cargo)