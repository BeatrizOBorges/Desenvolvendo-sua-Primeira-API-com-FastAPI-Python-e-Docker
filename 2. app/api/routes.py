rom fastapi import APIRouter, HTTPException
from app.models.product import ProductCreate, ProductUpdate
from app.services.product_service import ProductService
from app.repositories.mongo_repo import MongoProductRepository

router = APIRouter()
service = ProductService(MongoProductRepository())

@router.post("/products/", status_code=201)
async def create_product(product: ProductCreate):
    try:
        return await service.create_product(product)
    except Exception:
        raise HTTPException(status_code=400, detail="Erro ao criar produto")

@router.patch("/products/{id}")
async def update_product(id: str, product: ProductUpdate):
    try:
        return await service.update_product(id, product)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
