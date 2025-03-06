from routers.base import BaseRouter
from services.cargo import CargoService
from schemas.cargo import CargoCreate, CargoUpdate, CargoResponse

router = BaseRouter(CargoService, CargoCreate, CargoUpdate, CargoResponse, "cargo").router