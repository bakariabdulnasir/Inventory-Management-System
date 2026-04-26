from app.authentication.model.role_model import Role

def validate_register(data):
    errors = []

    # 🧱 Required fields
    if not data or not isinstance(data, dict):
        return ["Invalid request body"]

    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")
    role_name = data.get("role", "").strip()

    # 👤 Username
    if not username:
        errors.append("Username is required")
    elif len(username) < 2:
        errors.append("Username must be at least 2 characters")

    # 📧 Email
    if not email:
        errors.append("Email is required")
    elif "@" not in email:
        errors.append("Invalid email format")

    # 🔐 Password
    if not password:
        errors.append("Password is required")
    elif len(password) < 4:
        errors.append("Password must be at least 4 characters")

    # 🔑 Role (NOW CHECKS DATABASE)
    if not role_name:
        errors.append("Role is required")
    else:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            errors.append(f"Role '{role_name}' does not exist")

    return errors