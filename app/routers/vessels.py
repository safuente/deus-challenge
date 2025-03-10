from routers.base import BaseRouter
from services.vessel import VesselService
from schemas.vessel import VesselCreate, VesselUpdate, VesselResponse

"""Router for Vessel endpoints using the BaseRouter abstraction."""
router = BaseRouter(
    service_class=VesselService,
    create_schema=VesselCreate,
    update_schema=VesselUpdate,
    response_schema=VesselResponse,
    model_name="vessel",
).router
