from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from core.database import Base


class Vessel(Base):
    """Represents a vessel entity, storing vessel details and tracking information."""

    __tablename__ = "vessels"

    vessel_id: int = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        doc="Unique identifier for the vessel.",
    )
    name: str = Column(String, index=True, nullable=False, doc="Name of the vessel.")
    capacity: float = Column(
        Float, nullable=False, doc="Capacity of the vessel in metric tons."
    )
    current_location: str = Column(
        String, nullable=False, doc="Current location of the vessel."
    )

    tracking = relationship(
        "Tracking",
        back_populates="vessel",
        doc="Tracking entries associated with this vessel.",
    )

    def __repr__(self) -> str:
        """String representation of the Vessel model."""
        return f"<Vessel(id={self.vessel_id}, name={self.name}, location={self.current_location})>"
