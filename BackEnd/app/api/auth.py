from fastapi import APIRouter
from app.schemas.auth import RegisterSchema, LoginSchema, TokenSchema
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
async def register(data: RegisterSchema):
    return await register_user(data)


@router.post("/login", response_model=TokenSchema)
async def login(data: LoginSchema):
    return await login_user(data)

@router.get("/health")
async def health_check():
    return {"status": "ok"}
