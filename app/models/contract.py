from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from core.database import Base


class Contract(Base):
    """Represents a contract entity, linking clients to cargo shipments."""

    __tablename__ = "contracts"

    contract_id: int = Column(Integer, primary_key=True, index=True, autoincrement=True,
                              doc="Unique identifier for the contract.")
    client_id: int = Column(Integer, ForeignKey("clients.client_id", ondelete="CASCADE"), nullable=False,
                            doc="Foreign key linking to the client.")
    destination: str = Column(String, nullable=False, doc="Destination of the shipment.")
    price: float = Column(Float, nullable=False, doc="Price of the contract.")
    start_date: datetime = Column(DateTime, default=datetime.utcnow, doc="Start date of the contract.")
    end_date: datetime | None = Column(DateTime, nullable=True, doc="End date of the contract (optional).")
    status: str = Column(String, default="active", doc="Current status of the contract.")

    client = relationship("Client", back_populates="contracts", doc="Client associated with this contract.")
    cargo = relationship("Cargo", uselist=False, back_populates="contract", doc="Cargo associated with this contract.")

    def __repr__(self) -> str:
        """String representation of the Contract model."""
        return f"<Contract(id={self.contract_id}, destination={self.destination}, status={self.status})>"
