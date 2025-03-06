from pydantic import BaseModel
from typing import Optional


class VesselBase(BaseModel):
    name: str
    capacity: float
    current_location: str

class VesselCreate(VesselBase):
    pass

class VesselUpdate(BaseModel):
    name: Optional[str] = None
    capacity: Optional[float] = None
    current_location: Optional[str] = None

class VesselResponse(VesselBase):
    vessel_id: int
    class Config:
        orm_mode = True
