from app.models.product import ProductCreate, ProductInDB, ProductUpdate
from datetime import datetime

class ProductService:
    def __init__(self, repository):
        self.repository = repository

    async def create_product(self, product_data: ProductCreate):
        data = product_data.dict()
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        return await self.repository.insert_product(data)

    async def update_product(self, id: str, product_data: ProductUpdate):
        existing = await self.repository.get_product(id)
        if not existing:
            raise ValueError("Produto não encontrado")

        product_data.updated_at = datetime.utcnow()
        return await self.repository.update_product(id, product_data.dict(exclude_unset=True))
