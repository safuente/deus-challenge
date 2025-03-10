from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from core.database import Base


class Cargo(Base):
    """Represents a cargo entity, linking shipments to contracts and tracking."""

    __tablename__ = "cargoes"

    cargo_id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description: str = Column(
        String, nullable=False, doc="Description of the cargo contents."
    )
    weight: float = Column(
        Float, nullable=False, doc="Weight of the cargo in kilograms."
    )
    volume: float = Column(
        Float, nullable=False, doc="Volume of the cargo in cubic meters."
    )
    contract_id: int = Column(
        Integer,
        ForeignKey("contracts.contract_id", ondelete="CASCADE"),
        nullable=False,
        doc="Associated contract ID.",
    )
    status: str = Column(String, default="pending", doc="Current status of the cargo.")

    contract = relationship("Contract", back_populates="cargo")
    tracking = relationship("Tracking", back_populates="cargo")

    def __repr__(self) -> str:
        """String representation of the Cargo model."""
        return f"<Cargo(id={self.cargo_id}, description={self.description}, status={self.status})>"
