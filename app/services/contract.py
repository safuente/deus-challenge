from models import Contract
from .base import BaseService


class ContractService(BaseService):
    def __init__(self, db):
        super().__init__(db, Contract)