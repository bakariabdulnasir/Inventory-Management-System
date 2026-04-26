from app import create_app
from app.database import db
from app.authentication.model.role_model import Role

app = create_app()

with app.app_context():

    roles = ["admin", "user", "manager", "staff"]

    for role_name in roles:
        existing = Role.query.filter_by(name=role_name).first()
        if not existing:
            db.session.add(Role(name=role_name))

    db.session.commit()
    print("Roles seeded successfully!")