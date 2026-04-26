from app.database import db
from app.mkg.model.product_model import Product
from app.mkg.model.category_model import Category


class ProductRepository:

    def create_product(self, name, price, category_name):

        category = Category.query.filter_by(name=category_name).first()

        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()

        product = Product(
            name=name,
            price=price,
            category=category
        )

        db.session.add(product)
        db.session.commit()

        return product

    def get_all_products(self):
        return Product.query.all()