import pytest
from rest_framework.test import APIClient
from rest_framework import status

def test_api_product_creation():
    client = APIClient()

    product_data = {
        "name": "Test Product",
        "price": 10,
        "brand": "Test Brand",
        "countInStock": 5,
        "category": "Test Category",
        "description": "Test Description"
    }

    response = client.post("/api/products/", product_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    # assert response.data['name'] == product_data['name']
    # assert response.data['price'] == product_data['price']
    # assert response.data['brand'] == product_data['brand']
    # assert response.data['countInStock'] == product_data['countInStock']
    # assert response.data['category'] == product_data['category']
    # assert response.data['description'] == product_data['description']

# # @pytest.mark.django_db
# # def test_product_created():
# #   Product.objects.create
# from rest_framework.reverse import reverse
# from rest_framework.test import APIClient

# from base.models import Product


# def create_product():
#   return Product.objects.create(
#         name=" Product Name ",
#         price=0,
#         brand="Sample brand ",
#         countInStock=0,
#         category="Sample category",
#         description=" ")

# @pytest.mark.django_db
# def test_product_creation():
#   p = create_product()
#   assert isinstance(p, Product) is True
#   assert p.name == " Product Name "





# # Api test  - Integration testing
# def test_api_product_creation():
#     client = APIClient()

#     response = client.post("/api/products/create/")

#     # data = response.data

#     assert response.status_code == 200
