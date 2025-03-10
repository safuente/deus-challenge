from pydantic import BaseModel
from typing import Optional


class CargoBase(BaseModel):
    """Base schema for Cargo, containing common attributes."""
    description: str
    weight: float
    volume: float
    contract_id: int
    status: Optional[str] = "pending"


class CargoCreate(CargoBase):
    """Schema for creating a new Cargo item."""
    pass


class CargoUpdate(BaseModel):
    """Schema for updating an existing Cargo item."""
    description: Optional[str] = None
    weight: Optional[float] = None
    volume: Optional[float] = None
    status: Optional[str] = None


class CargoResponse(CargoBase):
    """Schema for returning Cargo data in API responses."""
    cargo_id: int

    class Config:
        orm_mode = True