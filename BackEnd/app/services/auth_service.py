from app.db.mongodb import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import user_model
from fastapi import HTTPException, status


async def register_user(data):
    db = get_db()

    # Check existing user
    if await db.users.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    user = user_model({
        "name": data.name,
        "college": data.college,
        "age": data.age,
        "exam": data.exam,
        "branch": data.branch,
        "email": data.email,
        "phone": data.phone,
        "hashed_password": hash_password(data.password),
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
