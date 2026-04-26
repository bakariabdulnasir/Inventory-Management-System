from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.mkg.controllers.stock_transaction_controller import StockTransactionController

stock_tx_bp = Blueprint("stock_transactions", __name__, url_prefix="/stock-transactions")

controller = StockTransactionController()


@stock_tx_bp.route("/", methods=["POST"])
@jwt_required()
def create_transaction():
    return controller.create_transaction(request.get_json())