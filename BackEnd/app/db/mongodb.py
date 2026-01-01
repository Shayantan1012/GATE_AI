from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None

mongodb = MongoDB()

async def connect_db():
    mongodb.client = AsyncIOMotorClient(settings.MONGODB_URI)
    print("✅ MongoDB connected")

async def close_db():
    mongodb.client.close()
    print("❌ MongoDB disconnected")

def get_db():
    return mongodb.client[settings.MONGODB_DB_NAME]
