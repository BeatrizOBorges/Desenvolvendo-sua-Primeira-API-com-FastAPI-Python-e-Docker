from app.models.product import ProductCreate

def test_create_product_schema():
    product = ProductCreate(name="Notebook", price=6000.00)
    assert product.name == "Notebook"
    assert product.price == 6000.00
