from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship, Session

from core.database import Base


class Contract(Base):
    __tablename__ = "contracts"
    contract_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"))
    destination = Column(String)
    price = Column(Float)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    status = Column(String, default="active")
    client = relationship("Client", back_populates="contracts")
    cargo = relationship("Cargo", uselist=False, back_populates="contract")
