from datetime import datetime

def user_model(data: dict):
    return {
        "name": data["name"],
        "college": data["college"],
        "age": data["age"],
        "exam": data["exam"],          # GATE / CAT / UPSC etc.
        "branch": data["branch"],
        "email": data["email"],
        "phone": data["phone"],
        "hashed_password": data["hashed_password"],
        "role": data.get("role", "user"),
        "is_active": True,
        "created_at": datetime.utcnow()
    }
