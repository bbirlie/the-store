from database import db
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


class TagModel(Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(db.Integer(), db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="item_tags")
