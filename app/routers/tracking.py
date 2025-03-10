from routers.base import BaseRouter
from services.tracking import TrackingService
from schemas.tracking import TrackingCreate, TrackingUpdate, TrackingResponse

"""Router for Tracking endpoints using the BaseRouter abstraction."""
router = BaseRouter(
    service_class=TrackingService,
    create_schema=TrackingCreate,
    update_schema=TrackingUpdate,
    response_schema=TrackingResponse,
    model_name="tracking",
).router
