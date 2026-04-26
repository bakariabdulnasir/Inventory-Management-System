from app.view.api_response import success_response, error_response
from app.authentication.model.user_repository import UserRepository
from app.authentication.schema.auth_schema import UserSchema, RegisterSchema
from flask_jwt_extended import create_access_token


class AuthController:

    def __init__(self):
        self.user_repo = UserRepository()
        self.user_schema = UserSchema()
        self.register_schema = RegisterSchema()

    #  REGISTER
    def register_user(self, data):

        # 🔥 VALIDATE USING MARSHMALLOW
        errors = self.register_schema.validate(data)
        if errors:
            return error_response(errors), 400

        # check existing user
        existing_user = self.user_repo.get_user_by_username_or_email(data["email"])
        if existing_user:
            return error_response("User already exists"), 400

        # create user
        user = self.user_repo.create_user(
            data["username"],
            data["email"],
            data["password"],
            data["role"]
        )

        # 🔥 SERIALIZE USING MARSHMALLOW
        return success_response(
            "User registered successfully",
            self.user_schema.dump(user)
        ), 201

    # LOGIN 
    def login_user(self, data):

        identifier = data.get("username") or data.get("email")

        if not identifier or not data.get("password"):
            return error_response("All fields are required"), 400

        user = self.user_repo.get_user_by_username_or_email(identifier)

        if not user or user.password != data["password"]:
            return error_response("Invalid credentials"), 401

        # Create access token
        access_token = create_access_token(
             identity=str(user.id),   # 🔥 FIX
           additional_claims={"role": user.role.name}
          )
        return success_response(
            "Login successful",
            {
                "user": self.user_schema.dump(user),
                "access_token": access_token
            }
        ), 200