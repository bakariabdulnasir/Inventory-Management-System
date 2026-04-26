from app.database import db

class Stock(db.Model):
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=0)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), unique=True)
    product = db.relationship("Product", backref="stock")