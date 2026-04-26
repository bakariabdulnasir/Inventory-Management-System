from app.mkg.model.inventory_model import Inventory
from app.mkg.model.stock_transaction_model import StockTransaction
from app.database import db


class StockController:

    def update_stock(self, data):
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        transaction_type = data.get("type")  # "in" or "out"

        if not product_id or not quantity or not transaction_type:
            return {"error": "All fields required"}, 400

        inventory = Inventory.query.filter_by(product_id=product_id).first()

        if not inventory:
            return {"error": "Inventory not found"}, 404

        # 🔥 STOCK LOGIC
        if transaction_type == "in":
            inventory.quantity += quantity

        elif transaction_type == "out":
            if inventory.quantity < quantity:
                return {"error": "Not enough stock"}, 400
            inventory.quantity -= quantity

        else:
            return {"error": "Invalid type"}, 400

        # save transaction
        transaction = StockTransaction(
            product_id=product_id,
            quantity=quantity,
            type=transaction_type
        )

        db.session.add(transaction)
        db.session.commit()

        return {
            "message": "Stock updated",
            "new_quantity": inventory.quantity
        }, 200