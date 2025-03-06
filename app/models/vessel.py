from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship, Session

from core.database import Base


class Vessel(Base):
    __tablename__ = "vessels"
    vessel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    capacity = Column(Float)
    current_location = Column(String)
    tracking = relationship("Tracking", back_populates="vessel")
