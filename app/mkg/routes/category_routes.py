from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.database import db
from app.mkg.model.category_model import Category

category_bp = Blueprint("categories", __name__, url_prefix="/categories")


@category_bp.route("/", methods=["POST"])
@jwt_required()
def create_category():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return {"status": "error", "message": "Name required"}, 400

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()

    return {"status": "success", "data": {"id": category.id, "name": name}}, 201


@category_bp.route("/", methods=["GET"])
@jwt_required()
def get_categories():
    categories = Category.query.all()

    return {
        "status": "success",
        "data": [{"id": c.id, "name": c.name} for c in categories]
    }, 200