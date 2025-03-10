from typing import Type
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Contract, Cargo
from services.base import BaseService
from pydantic import BaseModel

class CargoService(BaseService):
    def __init__(self, db: Session) -> None:
        """Initialize the CargoService with a database session."""
        super().__init__(db, Cargo)

    def create_item(self, item_data: BaseModel) -> Cargo:
        """Create a cargo item, ensuring the referenced contract exists."""
        contract_id: int | None = item_data.dict().get("contract_id")
        if contract_id is not None:
            contract: Contract | None = self.db.query(Contract).filter(Contract.contract_id == contract_id).first()
            if not contract:
                raise HTTPException(status_code=400, detail=f"Contract ID {contract_id} does not exist")

        return super().create_item(item_data)
