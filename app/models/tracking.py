from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship, Session

from core.database import Base


class Tracking(Base):
    __tablename__ = "tracking"
    tracking_id = Column(Integer, primary_key=True, index=True)
    cargo_id = Column(Integer, ForeignKey("cargoes.cargo_id"))
    vessel_id = Column(Integer, ForeignKey("vessels.vessel_id"))
    location = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String)
    cargo = relationship("Cargo", back_populates="tracking")
    vessel = relationship("Vessel", back_populates="tracking")