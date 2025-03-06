from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship, Session

from core.database import Base

class Cargo(Base):
    __tablename__ = "cargoes"
    cargo_id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    weight = Column(Float)
    volume = Column(Float)
    contract_id = Column(Integer, ForeignKey("contracts.contract_id"))
    status = Column(String, default="pending")
    contract = relationship("Contract", back_populates="cargo")
    tracking = relationship("Tracking", back_populates="cargo")