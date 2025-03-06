from pydantic import BaseModel
from datetime import datetime

class ClientBase(BaseModel):
    name: str
    contact_info: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class ClientResponse(ClientBase):
    client_id: int
    created_at: datetime
    class Config:
        orm_mode = True

