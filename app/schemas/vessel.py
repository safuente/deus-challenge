from pydantic import BaseModel
from typing import Optional


class VesselBase(BaseModel):
    """Base schema for Vessel, containing common attributes."""

    name: str
    capacity: float
    current_location: str


class VesselCreate(VesselBase):
    """Schema for creating a new Vessel."""

    pass


class VesselUpdate(BaseModel):
    """Schema for updating an existing Vessel."""

    name: Optional[str] = None
    capacity: Optional[float] = None
    current_location: Optional[str] = None


class VesselResponse(VesselBase):
    """Schema for returning Vessel data in API responses."""

    vessel_id: int

    class Config:
        orm_mode = True
