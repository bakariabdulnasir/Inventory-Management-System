from flask import Blueprint, request
from app.mkg.controllers.stock_controller import StockController

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")

controller = StockController()

@stock_bp.route("/", methods=["POST"])
def add_stock():
    return controller.add_stock(request.get_json())