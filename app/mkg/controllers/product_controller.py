from app.mkg.model.product_model import Product
from app.mkg.model.category_model import Category
from app.mkg.model.supplier_model import Supplier
from app.mkg.model.inventory_model import Inventory
from app.database import db


class ProductController:

    # 🔥 CREATE PRODUCT
    def create_product(self, data):
        try:
            name = data.get("name")
            price = data.get("price")
            category_name = data.get("category")
            supplier_id = data.get("supplier_id")

            # ✅ VALIDATION
            if not name or not price or not category_name or not supplier_id:
                return {"status": "error", "message": "All fields required"}, 400

            if price <= 0:
                return {"status": "error", "message": "Invalid price"}, 400

            # ✅ CATEGORY CHECK / CREATE
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db.session.add(category)
                db.session.commit()

            # ✅ SUPPLIER CHECK
            supplier = Supplier.query.get(supplier_id)
            if not supplier:
                return {"status": "error", "message": "Supplier not found"}, 404

            # ✅ CREATE PRODUCT
            product = Product(
                name=name,
                price=price,
                category_id=category.id,
                supplier_id=supplier.id
            )

            db.session.add(product)
            db.session.commit()  # 🔥 MUST COMMIT FIRST

            # ✅ CREATE INVENTORY AFTER PRODUCT EXISTS
            inventory = Inventory(
                product_id=product.id,
                quantity=0
            )

            db.session.add(inventory)
            db.session.commit()

            return {
                "status": "success",
                "data": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "category": category.name,
                    "supplier": supplier.name,
                    "quantity": inventory.quantity
                }
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"status": "error", "message": str(e)}, 500

    # 📦 GET ALL PRODUCTS
    def get_products(self):
        try:
            products = Product.query.all()

            return {
                "status": "success",
                "data": [
                    {
                        "id": p.id,
                        "name": p.name,
                        "price": p.price,
                        "category": p.category.name if p.category else None,
                        "supplier": p.supplier.name if p.supplier else None,
                        "quantity": p.inventory.quantity if p.inventory else 0
                    } for p in products
                ]
            }, 200

        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    # 🔍 GET SINGLE PRODUCT
    def get_product(self, product_id):
        try:
            product = Product.query.get(product_id)

            if not product:
                return {"status": "error", "message": "Product not found"}, 404

            return {
                "status": "success",
                "data": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "category": product.category.name if product.category else None,
                    "supplier": product.supplier.name if product.supplier else None,
                    "quantity": product.inventory.quantity if product.inventory else 0
                }
            }, 200

        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    # ✏️ UPDATE PRODUCT
    def update_product(self, product_id, data):
        try:
            product = Product.query.get(product_id)

            if not product:
                return {"status": "error", "message": "Product not found"}, 404

            name = data.get("name")
            price = data.get("price")
            category_name = data.get("category")
            supplier_id = data.get("supplier_id")

            # ✅ UPDATE NAME
            if name:
                product.name = name

            # ✅ UPDATE PRICE
            if price:
                if price <= 0:
                    return {"status": "error", "message": "Invalid price"}, 400
                product.price = price

            # ✅ UPDATE CATEGORY
            if category_name:
                category = Category.query.filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    db.session.add(category)
                    db.session.commit()
                product.category_id = category.id

            # ✅ UPDATE SUPPLIER
            if supplier_id:
                supplier = Supplier.query.get(supplier_id)
                if not supplier:
                    return {"status": "error", "message": "Supplier not found"}, 404
                product.supplier_id = supplier.id

            db.session.commit()

            return {
                "status": "success",
                "message": "Product updated"
            }, 200

        except Exception as e:
            db.session.rollback()
            return {"status": "error", "message": str(e)}, 500

    # 🗑 DELETE PRODUCT
    def delete_product(self, product_id):
        try:
            product = Product.query.get(product_id)

            if not product:
                return {"status": "error", "message": "Product not found"}, 404

            # ✅ ALSO DELETE INVENTORY (IMPORTANT)
            if product.inventory:
                db.session.delete(product.inventory)

            db.session.delete(product)
            db.session.commit()

            return {
                "status": "success",
                "message": "Product deleted"
            }, 200

        except Exception as e:
            db.session.rollback()
            return {"status": "error", "message": str(e)}, 500