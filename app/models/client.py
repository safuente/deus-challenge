from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from core.database import Base


class Client(Base):
    """Represents a client entity, storing client details and associated contracts."""

    __tablename__ = "clients"

    client_id: int = Column(Integer, primary_key=True, index=True, autoincrement=True,
                            doc="Unique identifier for the client.")
    name: str = Column(String, index=True, nullable=False, doc="Name of the client.")
    contact_info: str = Column(String, nullable=False, doc="Contact details of the client.")
    created_at: datetime = Column(DateTime, default=datetime.utcnow, doc="Timestamp when the client was created.")

    contracts = relationship("Contract", back_populates="client", doc="List of contracts associated with the client.")

    def __repr__(self) -> str:
        """String representation of the Client model."""
        return f"<Client(id={self.client_id}, name={self.name})>"