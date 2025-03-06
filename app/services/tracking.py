from models import Tracking
from .base import BaseService


class TrackingService(BaseService):
    def __init__(self, db):
        super().__init__(db, Tracking)