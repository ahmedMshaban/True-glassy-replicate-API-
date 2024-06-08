from django.urls import reverse
from rest_framework.test import APITestCase
from .factories import BrandFactory, LineFactory, ProductFactory


class CrueltyFreeVeganProductsViewTest(APITestCase):

    def setUp(self):
        self.brand = BrandFactory.create()
        self.line = LineFactory.create()
        self.product1 = ProductFactory.create(
            brand=self.brand, line=self.line, cruelty_free=True, vegan=True
        )
        self.product2 = ProductFactory.create(
            brand=self.brand, line=self.line, cruelty_free=False, vegan=True
        )
        self.product3 = ProductFactory.create(
            brand=self.brand, line=self.line, cruelty_free=True, vegan=False
        )
        self.product4 = ProductFactory.create(
            brand=self.brand, line=self.line, cruelty_free=True, vegan=True
        )
        self.url = reverse(
            "cruelty_free_vegan_products",
            kwargs={"brand_id": self.brand.id, "line_id": self.line.id},
        )

    def test_get_cruelty_free_vegan_products_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_cruelty_free_vegan_products_no_match(self):
        new_brand = BrandFactory.create()
        new_line = LineFactory.create()
        url = reverse(
            "cruelty_free_vegan_products",
            kwargs={"brand_id": new_brand.id, "line_id": new_line.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
