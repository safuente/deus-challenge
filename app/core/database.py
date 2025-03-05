from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine("sqlite:///temp_db.sqlite", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()