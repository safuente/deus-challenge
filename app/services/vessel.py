from sqlalchemy.orm import Session
from models import Vessel
from services.base import BaseService


class VesselService(BaseService):
    def __init__(self, db: Session) -> None:
        """Initialize the VesselService with a database session."""
        super().__init__(db, Vessel)
