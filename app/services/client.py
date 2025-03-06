from models import Client
from .base import BaseService


class ClientService(BaseService):
    def __init__(self, db):
        super().__init__(db, Client)