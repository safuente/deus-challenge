from typing import Type
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.sql import text
from models import Contract, Cargo, Client
from services.base import BaseService
from pydantic import BaseModel


class ContractService(BaseService):
    def __init__(self, db: Session) -> None:
        """Initialize the ContractService with a database session."""
        super().__init__(db, Contract)

    def create_item(self, item_data: BaseModel) -> Contract:
        """Create a contract, ensuring the referenced client exists."""
        client_id: int | None = item_data.dict().get("client_id")
        if client_id is not None:
            client: Client | None = (
                self.db.query(Client).filter(Client.client_id == client_id).first()
            )
            if not client:
                raise HTTPException(
                    status_code=400, detail=f"Client ID {client_id} does not exist"
                )

        return super().create_item(item_data)
