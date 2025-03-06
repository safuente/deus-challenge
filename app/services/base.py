from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.sql import text

class BaseService:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def create_item(self, item_data):
        item = self.model(**item_data.dict())
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def list_items(self, order_by=None):
        order_by = text(f"{self.model.__name__.lower()}_id") if order_by is None else text(order_by)
        return self.db.query(self.model).order_by(order_by).all()

    def get_item(self, item_id: int):
        primary_key_field = getattr(self.model, f"{self.model.__name__.lower()}_id")
        item = self.db.query(self.model).filter(primary_key_field == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} with ID {item_id} not found")
        return item

    def update_item(self, item_id: int, item_data):
        item = self.db.query(self.model).filter(
            getattr(self.model, f"{self.model.__name__.lower()}_id") == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} with ID {item_id} not found")

        for key, value in item_data.dict(exclude_unset=True).items():
            setattr(item, key, value)

        self.db.commit()
        self.db.refresh(item)
        return item

    def delete_item(self, item_id: int):
        item = self.db.query(self.model).filter(
            getattr(self.model, f"{self.model.__name__.lower()}_id") == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} with ID {item_id} not found")
        self.db.delete(item)
        self.db.commit()
        return {"message": f"{self.model.__name__} with ID {item_id} deleted successfully"}