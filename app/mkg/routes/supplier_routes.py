from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.mkg.controllers.supplier_controller import SupplierController

supplier_bp = Blueprint("suppliers", __name__, url_prefix="/suppliers")
controller = SupplierController()


@supplier_bp.route("/", methods=["POST"])
@jwt_required()
def create_supplier():
    return controller.create_supplier(request.get_json())


@supplier_bp.route("/", methods=["GET"])
@jwt_required()
def get_suppliers():
    return controller.get_suppliers()


@supplier_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_supplier(id):
    return controller.delete_supplier(id)