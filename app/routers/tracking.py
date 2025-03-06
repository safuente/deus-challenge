from routers.base import BaseRouter
from services.tracking import TrackingService
from schemas.tracking import TrackingCreate, TrackingUpdate, TrackingResponse

router = BaseRouter(TrackingService, TrackingCreate, TrackingUpdate, TrackingResponse, "tracking").router
