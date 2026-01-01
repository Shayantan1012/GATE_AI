from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.db.mongodb import connect_db, close_db

app = FastAPI(title="GATE AI Backend")

@app.on_event("startup")
async def startup_db():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db():
    await close_db()
    

app.include_router(auth_router)

