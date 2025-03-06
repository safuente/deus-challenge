import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

DB_PATH = os.path.join("database.sqlite")

# Definir la URL de la base de datos
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
#engine = create_engine("sqlite:///temp_db.sqlite", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()