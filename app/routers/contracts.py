from routers.base import BaseRouter
from services.contract import ContractService
from schemas.contract import ContractCreate, ContractUpdate, ContractResponse

router = BaseRouter(ContractService, ContractCreate, ContractUpdate, ContractResponse, "contract").router