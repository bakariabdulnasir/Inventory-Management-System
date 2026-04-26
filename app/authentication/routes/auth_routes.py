from flask import Blueprint, request
from app.authentication.controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__)

controller = AuthController()

@auth_bp.route("/register", methods=["POST"])
def register():
    return controller.register_user(request.get_json())

@auth_bp.route("/login", methods=["POST"])
def login():
    return controller.login_user(request.get_json())