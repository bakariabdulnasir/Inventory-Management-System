from flask import Blueprint, request
from app.mkg.controllers.product_controller import ProductController
from app.utils.role_required import role_required
from flask_jwt_extended import jwt_required


product_bp = Blueprint("products", __name__, url_prefix="/products")

controller = ProductController()


# CREATE
@product_bp.route("/", methods=["POST"])
#admin only route 
@jwt_required()
@role_required("admin")


def create_product():
    return controller.create_product(request.get_json())


# READ ALL
@product_bp.route("/", methods=["GET"])
def get_products():
    return controller.get_products()


# READ ONE
@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return controller.get_product(product_id)


# UPDATE
@product_bp.route("/<int:product_id>", methods=["PUT"])
@jwt_required()
@role_required("admin")

def update_product(product_id):
    return controller.update_product(product_id, request.get_json())


# DELETE
@product_bp.route("/<int:product_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin") 

def delete_product(product_id):
    return controller.delete_product(product_id)