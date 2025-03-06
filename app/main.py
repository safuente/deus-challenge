from fastapi import FastAPI
#from app.api.routes import contracts, cargoes, vessels, tracking
from core.database import Base, engine, SessionLocal

app = FastAPI(
    title="DEUS API CHALLENGE",
    version="1.0"
)


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Deus challenge API is running!"}