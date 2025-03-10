from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ContractBase(BaseModel):
    """Base schema for Contract, containing common attributes."""
    client_id: int
    destination: str
    price: float
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = "active"


class ContractCreate(ContractBase):
    """Schema for creating a new Contract."""
    pass


class ContractUpdate(BaseModel):
    """Schema for updating an existing Contract."""
    destination: Optional[str] = None
    price: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None


class ContractResponse(ContractBase):
    """Schema for returning Contract data in API responses."""
    contract_id: int

    class Config:
        orm_mode = True