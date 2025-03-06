from routers.base import BaseRouter
from services.vessel import VesselService
from schemas.vessel import VesselCreate, VesselUpdate, VesselResponse

router = BaseRouter(VesselService, VesselCreate, VesselUpdate, VesselResponse, "vessel").router
