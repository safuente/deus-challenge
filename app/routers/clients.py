from routers.base import BaseRouter
from services.client import ClientService
from schemas.client import ClientCreate, ClientUpdate, ClientResponse

router = BaseRouter(ClientService, ClientCreate, ClientUpdate, ClientResponse, "client").router