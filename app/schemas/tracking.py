from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TrackingBase(BaseModel):
    cargo_id: int
    vessel_id: Optional[int] = None
    location: str
    updated_at: Optional[datetime] = None
    status: str

class TrackingCreate(TrackingBase):
    pass

class TrackingUpdate(BaseModel):
    location: Optional[str] = None
    updated_at: Optional[datetime] = None
    status: Optional[str] = None

class TrackingResponse(TrackingBase):
    tracking_id: int
    class Config:
        orm_mode = True