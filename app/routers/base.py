from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from typing import List, Type, TypeVar, Callable
from core.database import get_db
from pydantic import BaseModel

ServiceType = TypeVar("ServiceType")
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseRouter:
    """Base class for routers"""
    def __init__(
        self,
        service_class: Type[ServiceType],
        create_schema: Type[SchemaType],
        update_schema: Type[SchemaType] | None = None,
        response_schema: Type[SchemaType] | None = None,
        model_name: str = "item"
    ) -> None:
        """Initialize the BaseRouter with service class and schemas."""
        self.router = APIRouter()
        self.service_class = service_class
        self.model_name = model_name.lower()
        self.create_schema = create_schema
        self.update_schema = update_schema or create_schema
        self.response_schema = response_schema or create_schema
        self.set_routes()

    def set_routes(self) -> None:
        """Define and set API routes for CRUD operations."""

        @self.router.post("/", summary=f"Create {self.model_name}", description=f"Creates a new {self.model_name}.")
        def create_item(item: self.create_schema, db: Session = Depends(get_db)):
            return self.service_class(db).create_item(item)

        @self.router.put(f"/{{{self.model_name}_id}}", summary=f"Update {self.model_name}",
                         description=f"Updates an existing {self.model_name}.")
        def update_item(
            item: self.update_schema,
            item_id: int = Path(..., alias=f"{self.model_name}_id", description=f"ID of the {self.model_name}"),
            db: Session = Depends(get_db)
        ):
            return self.service_class(db).update_item(item_id, item)

        @self.router.get(f"/{{{self.model_name}_id}}", response_model=self.response_schema,
                         summary=f"Get {self.model_name}", description=f"Retrieves a {self.model_name} by its ID.")
        def get_item(
            item_id: int = Path(..., alias=f"{self.model_name}_id", description=f"ID of the {self.model_name}"),
            db: Session = Depends(get_db)
        ):
            return self.service_class(db).get_item(item_id)

        @self.router.get("/", response_model=List[self.response_schema], summary=f"List {self.model_name}s",
                         description=f"Returns a list of {self.model_name}s.")
        def list_items(db: Session = Depends(get_db)):
            return self.service_class(db).list_items()

        @self.router.delete(f"/{{{self.model_name}_id}}", summary=f"Delete {self.model_name}",
                            description=f"Deletes a {self.model_name} by its ID.")
        def delete_item(
            item_id: int = Path(..., alias=f"{self.model_name}_id", description=f"ID of the {self.model_name}"),
            db: Session = Depends(get_db)
        ):
            return self.service_class(db).delete_item(item_id)