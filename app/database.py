from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()   # ✅ ADD THIS

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userrbac.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)   # ✅ ADD THIS