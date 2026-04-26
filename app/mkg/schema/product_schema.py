from app.database import ma
from app.mkg.model.product_model import Product
from marshmallow import fields, validates, ValidationError

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

    category = ma.Function(lambda obj: obj.category.name if obj.category else None)


class CreateProductSchema(ma.Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)
    category = fields.String(required=True)

    @validates("price")
    def validate_price(self, value, **kwargs):
        if value <= 0:
            raise ValidationError("Price must be greater than 0")