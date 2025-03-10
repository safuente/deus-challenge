from routers.base import BaseRouter
from services.contract import ContractService
from schemas.contract import ContractCreate, ContractUpdate, ContractResponse

"""Router for Contract endpoints using the BaseRouter abstraction."""
router = BaseRouter(
    service_class=ContractService,
    create_schema=ContractCreate,
    update_schema=ContractUpdate,
    response_schema=ContractResponse,
    model_name="contract",
).router
