from app.database import db
from app.authentication.model.user_model import User
from app.authentication.model.role_model import Role

class UserRepository:

    def create_user(self, username, email, password, role_name):
        role = Role.query.filter_by(name=role_name).first()

        if not role:
            raise ValueError("Invalid role")

        user = User(
            username=username,
            email=email,
            password=password,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        return user

    
    def get_user_by_username_or_email(self, identifier):
        return User.query.filter(
            (User.username == identifier) | (User.email == identifier)
        ).first()

    def get_user_by_id(self, user_id):
        return db.session.get(User, user_id)