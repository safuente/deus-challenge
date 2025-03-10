from typing import Type
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Tracking, Cargo, Vessel
from services.base import BaseService
from pydantic import BaseModel


class TrackingService(BaseService):
    def __init__(self, db: Session) -> None:
        """Initialize the TrackingService with a database session."""
        super().__init__(db, Tracking)

    def create_item(self, item_data: BaseModel) -> Tracking:
        """Create a tracking entry, ensuring referenced cargo and vessel exist."""
        cargo_id: int | None = item_data.dict().get("cargo_id")
        if cargo_id is not None:
            cargo: Cargo | None = (
                self.db.query(Cargo).filter(Cargo.cargo_id == cargo_id).first()
            )
            if not cargo:
                raise HTTPException(
                    status_code=400, detail=f"Cargo ID {cargo_id} does not exist"
                )

        vessel_id: int | None = item_data.dict().get("vessel_id")
        if vessel_id is not None:
            vessel: Vessel | None = (
                self.db.query(Vessel).filter(Vessel.vessel_id == vessel_id).first()
            )
            if not vessel:
                raise HTTPException(
                    status_code=400, detail=f"Vessel ID {vessel_id} does not exist"
                )

        return super().create_item(item_data)
