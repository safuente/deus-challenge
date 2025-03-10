from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Client, Contract
from services.base import BaseService


class ClientService(BaseService):
    def __init__(self, db: Session) -> None:
        """Initialize the ClientService with a database session."""
        super().__init__(db, Client)

    def delete_item(self, item_id: int) -> dict[str, str]:
        """Prevents deletion if the client has associated contracts."""
        existing_contracts: Contract | None = (
            self.db.query(Contract).filter(Contract.client_id == item_id).first()
        )
        if existing_contracts:
            raise HTTPException(
                status_code=400, detail="Cannot delete client with active contracts"
            )

        return super().delete_item(item_id)
