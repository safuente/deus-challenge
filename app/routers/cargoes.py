from routers.base import BaseRouter
from services.cargo import CargoService
from schemas.cargo import CargoCreate, CargoUpdate, CargoResponse

"""Router for Cargo endpoints using the BaseRouter abstraction."""
router = BaseRouter(
    service_class=CargoService,
    create_schema=CargoCreate,
    update_schema=CargoUpdate,
    response_schema=CargoResponse,
    model_name="cargo"
).router
