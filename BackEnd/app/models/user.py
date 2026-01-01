from datetime import datetime

def user_model(user: dict):
    return {
        "email": user["email"],
        "hashed_password": user["hashed_password"],
        "role": user.get("role", "user"),  # user | admin
        "is_active": True,
        "created_at": datetime.utcnow()
    }
