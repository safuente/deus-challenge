from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum as SAEnum
from datetime import datetime
from sqlalchemy.orm import relationship
from core.database import Base
import enum


class TrackingStatus(str, enum.Enum):
    PENDING = "pending"
    IN_TRANSIT = "in transit"
    DELIVERED = "delivered"


class Tracking(Base):
    """Represents a tracking entry, linking cargo to vessel locations."""

    __tablename__ = "tracking"

    tracking_id: int = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        doc="Unique identifier for the tracking entry.",
    )
    cargo_id: int = Column(
        Integer,
        ForeignKey("cargoes.cargo_id"),
        nullable=False,
        doc="Foreign key linking to the cargo being tracked.",
    )
    vessel_id: int | None = Column(
        Integer,
        ForeignKey("vessels.vessel_id"),
        nullable=False,
        doc="Foreign key linking to the vessel carrying the cargo.",
    )
    location: str = Column(String, nullable=False, doc="Current location of the cargo.")
    updated_at: datetime = Column(
        DateTime, default=datetime.utcnow, doc="Timestamp of the last update."
    )
    status: TrackingStatus = Column(
        SAEnum(TrackingStatus),
        nullable=False,
        default=TrackingStatus.PENDING,
        doc="Current status of the cargo.",
    )

    cargo = relationship(
        "Cargo",
        back_populates="tracking",
        doc="Cargo associated with this tracking entry.",
    )
    vessel = relationship(
        "Vessel",
        back_populates="tracking",
        doc="Vessel associated with this tracking entry.",
    )

    def __repr__(self) -> str:
        """String representation of the Tracking model."""
        return f"<Tracking(id={self.tracking_id}, location={self.location}, status={self.status})>"
