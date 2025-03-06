from pydantic import BaseModel
from typing import Optional


class CargoBase(BaseModel):
    description: str
    weight: float
    volume: float
    contract_id: int
    status: Optional[str] = "pending"

class CargoCreate(CargoBase):
    pass

class CargoUpdate(BaseModel):
    description: Optional[str] = None
    weight: Optional[float] = None
    volume: Optional[float] = None
    status: Optional[str] = None

class CargoResponse(CargoBase):
    cargo_id: int
    class Config:
        orm_mode = True
