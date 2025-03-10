from pydantic import BaseModel
from datetime import datetime


class ClientBase(BaseModel):
    """Base schema for Client, containing common attributes."""
    name: str
    contact_info: str


class ClientCreate(ClientBase):
    """Schema for creating a new Client."""
    pass


class ClientUpdate(ClientBase):
    """Schema for updating an existing Client."""
    pass


class ClientResponse(ClientBase):
    """Schema for returning Client data in API responses."""
    client_id: int
    created_at: datetime

    class Config:
        orm_mode = True
