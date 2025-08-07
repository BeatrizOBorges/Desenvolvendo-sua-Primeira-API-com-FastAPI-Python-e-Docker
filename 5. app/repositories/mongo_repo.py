from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["store"]
collection = db["products"]

class MongoProductRepository:
    async def insert_product(self, product_data: dict):
        result = await collection.insert_one(product_data)
        return {"id": str(result.inserted_id)}

    async def get_product(self, id: str):
        return await collection.find_one({"_id": id})

    async def update_product(self, id: str, update_data: dict):
        await collection.update_one({"_id": id}, {"$set": update_data})
        return await self.get_product(id)
