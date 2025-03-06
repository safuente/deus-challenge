from fastapi import FastAPI
from core.database import Base, engine, SessionLocal
from routers import contract_router, client_router, cargoes_router, tracking_router, vessel_router


app = FastAPI(
    title="DEUS API CHALLENGE",
    version="1.0"
)


Base.metadata.create_all(bind=engine)


app.include_router(client_router, prefix="/clients", tags=["Clients"])
app.include_router(contract_router, prefix="/contracts", tags=["Contracts"])
app.include_router(cargoes_router, prefix="/cargoes", tags=["Cargoes"])
app.include_router(tracking_router, prefix="/tracking", tags=["Tracking"])
app.include_router(tracking_router, prefix="/vessels", tags=["Vessels"])

@app.get("/")
def root():
    return {"message": "Deus challenge API is running!"}