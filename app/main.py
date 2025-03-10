import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from core.database import Base, engine
from core.logger import logger
from routers import (
    contract_router,
    client_router,
    cargoes_router,
    tracking_router,
    vessel_router,
)

# Initialize FastAPI application with metadata
app = FastAPI(
    title="DEUS API CHALLENGE",
    version="1.0",
    description="An API designed for managing clients, contracts, cargoes, tracking, and vessels in a shipping system.",
    docs_url="/",
)

# Create database tables
Base.metadata.create_all(bind=engine)
logger.info("Database tables created.")

# Include API routers
app.include_router(client_router, prefix="/clients", tags=["Clients"])
app.include_router(contract_router, prefix="/contracts", tags=["Contracts"])
app.include_router(cargoes_router, prefix="/cargoes", tags=["Cargoes"])
app.include_router(tracking_router, prefix="/tracking", tags=["Tracking"])
app.include_router(vessel_router, prefix="/vessels", tags=["Vessels"])
logger.info("API routers registered.")


@app.get("/redirect", include_in_schema=False)
def redirect_to_docs():
    """Redirect to the API documentation."""
    logger.info("Redirecting to /docs")
    return RedirectResponse(url="/docs")
