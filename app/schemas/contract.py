from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContractBase(BaseModel):
    client_id: int
    destination: str
    price: float
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = "active"

class ContractCreate(ContractBase):
    pass

class ContractUpdate(BaseModel):
    destination: Optional[str] = None
    price: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None

class ContractResponse(ContractBase):
    contract_id: int
    class Config:
        orm_mode = True

class ContractResponse(ContractBase):
    contract_id: int
    class Config:
        orm_mode = True