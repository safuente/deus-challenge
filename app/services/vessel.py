from models import Vessel
from .base import BaseService


class VesselService(BaseService):
    def __init__(self, db):
        super().__init__(db, Vessel)