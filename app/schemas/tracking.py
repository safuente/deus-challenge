from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from models.tracking import TrackingStatus


class TrackingBase(BaseModel):
    """Base schema for Tracking, containing common attributes."""

    cargo_id: int
    vessel_id: Optional[int] = None
    location: str
    updated_at: Optional[datetime] = None
    status: Optional[TrackingStatus] = None


class TrackingCreate(TrackingBase):
    """Schema for creating a new Tracking entry."""

    pass


class TrackingUpdate(BaseModel):
    """Schema for updating an existing Tracking entry."""

    location: Optional[str] = None
    updated_at: Optional[datetime] = None
    status: Optional[TrackingStatus] = None


class TrackingResponse(TrackingBase):
    """Schema for returning Tracking data in API responses."""

    tracking_id: int

    class Config:
        orm_mode = True
