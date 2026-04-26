from flask import Flask
from datetime import timedelta

from app.database import init_db
from flask_jwt_extended import JWTManager

# 🔐 AUTH ROUTES
from app.authentication.routes.auth_routes import auth_bp

# 🔐 AUTH MODELS (🔥 YOU MISSED THESE)
from app.authentication.model.user_model import User
from app.authentication.model.role_model import Role

# 📦 MKG ROUTES
from app.mkg.routes.product_routes import product_bp
from app.mkg.routes.category_routes import category_bp
from app.mkg.routes.supplier_routes import supplier_bp
from app.mkg.routes.stock_routes import stock_bp
from app.mkg.routes.stock_transaction_routes import stock_tx_bp

# 📦 MKG MODELS
from app.mkg.model.product_model import Product
from app.mkg.model.category_model import Category
from app.mkg.model.supplier_model import Supplier
from app.mkg.model.inventory_model import Inventory
from app.mkg.model.stock_transaction_model import StockTransaction


def create_app():
    app = Flask(__name__)

    # 🔐 JWT CONFIG
    app.config["JWT_SECRET_KEY"] = "super-secret-key-that-is-long-enough-123456"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

    # 🗄️ DATABASE
    init_db(app)

    # 🔐 JWT INIT
    JWTManager(app)

    # 🔐 AUTH ROUTES
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # 📦 MKG ROUTES
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(supplier_bp)
    app.register_blueprint(stock_bp)
    app.register_blueprint(stock_tx_bp)  # 🔥 YOU ALSO FORGOT THIS

    return app