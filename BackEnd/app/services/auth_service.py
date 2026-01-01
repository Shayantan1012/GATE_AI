from app.db.mongodb import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import user_model
from fastapi import HTTPException, status


async def register_user(data):
    db = get_db()
    existing = await db.users.find_one({"email": data.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = user_model({
        "email": data.email,
        "hashed_password": hash_password(data.password),
        "role": "user"
    })

    await db.users.insert_one(user)
    return {"message": "User registered successfully"}


async def login_user(data):
    db = get_db()
    user = await db.users.find_one({"email": data.email})

    if not user or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {"sub": user["email"], "role": user["role"]}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }
