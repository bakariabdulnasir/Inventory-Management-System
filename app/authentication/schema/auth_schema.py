from app.database import ma
from app.authentication.model.user_model import User
from app.authentication.model.role_model import Role
from marshmallow import fields, validates, ValidationError


# 🔹 SERIALIZATION SCHEMA
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    # show role name instead of object
    role = ma.Function(lambda obj: obj.role.name if obj.role else None)


# 🔹 VALIDATION SCHEMA
class RegisterSchema(ma.Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

    from app.database import ma
from app.authentication.model.user_model import User
from app.authentication.model.role_model import Role
from marshmallow import fields, validates, ValidationError


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    role = ma.Function(lambda obj: obj.role.name if obj.role else None)


class RegisterSchema(ma.Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

    @validates("role")
    def validate_role(self, value, **kwargs):  # ✅ FIX HERE
        role = Role.query.filter_by(name=value).first()
        if not role:
            raise ValidationError("Invalid role")