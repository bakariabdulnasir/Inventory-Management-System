from app.database import db
from app.mkg.model.stock_model import Stock
from app.mkg.model.product_model import Product
from app.mkg.model.stock_transaction_model import StockTransaction


class StockTransactionController:

    def create_transaction(self, data):
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        transaction_type = data.get("type")

        # 🔍 Validate input
        if not product_id or not quantity or not transaction_type:
            return {"status": "error", "message": "All fields required"}, 400

        if transaction_type not in ["IN", "OUT"]:
            return {"status": "error", "message": "Invalid transaction type"}, 400

        product = Product.query.get(product_id)
        if not product:
            return {"status": "error", "message": "Product not found"}, 404

        # 🔍 Get or create stock
        stock = Stock.query.filter_by(product_id=product_id).first()

        if not stock:
            stock = Stock(product_id=product_id, quantity=0)
            db.session.add(stock)

        # 🔥 BUSINESS LOGIC
        if transaction_type == "IN":
            stock.quantity += quantity

        elif transaction_type == "OUT":
            if stock.quantity < quantity:
                return {"status": "error", "message": "Not enough stock"}, 400
            stock.quantity -= quantity

        # 🧾 Save transaction
        transaction = StockTransaction(
            product_id=product_id,
            quantity=quantity,
            type=transaction_type
        )

        db.session.add(transaction)
        db.session.commit()

        return {
            "status": "success",
            "message": "Transaction completed",
            "data": {
                "product_id": product_id,
                "quantity": quantity,
                "type": transaction_type
            }
        }, 201