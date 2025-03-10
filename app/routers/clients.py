from routers.base import BaseRouter
from services.client import ClientService
from schemas.client import ClientCreate, ClientUpdate, ClientResponse

"""Router for Client endpoints using the BaseRouter abstraction."""
router = BaseRouter(
    service_class=ClientService,
    create_schema=ClientCreate,
    update_schema=ClientUpdate,
    response_schema=ClientResponse,
    model_name="client",
).router
