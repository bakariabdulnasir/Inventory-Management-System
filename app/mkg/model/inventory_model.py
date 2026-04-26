from app.database import db
from app.mkg.model.product_model import Product


class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), unique=True)
    quantity = db.Column(db.Integer, default=0)

    product = db.relationship("Product", backref="inventory", uselist=False)