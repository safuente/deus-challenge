from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship, Session

from core.database import Base


class Client(Base):
    __tablename__ = "clients"
    client_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    contracts = relationship("Contract", back_populates="client")