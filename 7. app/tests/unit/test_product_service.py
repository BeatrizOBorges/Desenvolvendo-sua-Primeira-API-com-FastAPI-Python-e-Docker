import pytest
from app.services.product_service import ProductService
from app.models.product import ProductCreate

@pytest.mark.asyncio
async def test_create_product(mocker):
    repo = mocker.Mock()
    repo.insert_product.return_value = {"id": "abc123"}
    service = ProductService(repo)

    product = ProductCreate(name="TV", price=5500)
    result = await service.create_product(product)
    assert result["id"] == "abc123"
