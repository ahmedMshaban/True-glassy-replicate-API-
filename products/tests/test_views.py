from django.urls import reverse
from rest_framework.test import APITestCase
from .factories import (
    BrandFactory,
    LineFactory,
    ProductFactory,
    IngredientFactory,
    ProductIngredientFactory,
)


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


class CommonIngredientsViewTest(APITestCase):

    def setUp(self):
        self.country_code = "KR"
        self.product1 = ProductFactory.create(country=self.country_code)
        self.product2 = ProductFactory.create(country=self.country_code)
        self.product3 = ProductFactory.create(country="US")

        self.ingredient1 = IngredientFactory.create(name="Ingredient1")
        self.ingredient2 = IngredientFactory.create(name="Ingredient2")

        ProductIngredientFactory.create(
            product=self.product1, ingredient=self.ingredient1
        )
        ProductIngredientFactory.create(
            product=self.product1, ingredient=self.ingredient2
        )
        ProductIngredientFactory.create(
            product=self.product2, ingredient=self.ingredient1
        )
        ProductIngredientFactory.create(
            product=self.product2, ingredient=self.ingredient2
        )
        ProductIngredientFactory.create(
            product=self.product3, ingredient=self.ingredient1
        )

        self.url = reverse("common_ingredients", kwargs={"country": self.country_code})

    def test_get_common_ingredients_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        ingredients = {
            item["ingredient__name"]: item["count"] for item in response.data
        }

        self.assertEqual(ingredients["Ingredient1"], 2)
        self.assertEqual(ingredients["Ingredient2"], 2)

    def test_get_common_ingredients_no_match(self):
        url = reverse("common_ingredients", kwargs={"country": "CN"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_get_common_ingredients_error(self):
        url = reverse("common_ingredients", kwargs={"country": "invalid"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)


class ProductsByIngredientViewTest(APITestCase):

    def setUp(self):
        self.ingredient = IngredientFactory.create(name="Test Ingredient")
        self.product1 = ProductFactory.create(name="Product 1")
        self.product2 = ProductFactory.create(name="Product 2")
        self.product3 = ProductFactory.create(name="Product 3")

        ProductIngredientFactory.create(
            product=self.product1, ingredient=self.ingredient, concentration_value=5.0
        )
        ProductIngredientFactory.create(
            product=self.product2, ingredient=self.ingredient, concentration_value=10.0
        )
        ProductIngredientFactory.create(
            product=self.product3, ingredient=self.ingredient, concentration_value=1.0
        )

        self.url = reverse(
            "products_by_ingredient", kwargs={"ingredient_id": self.ingredient.id}
        )

    def test_get_products_by_ingredient_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["name"], "Product 2")
        self.assertEqual(response.data[0]["concentration_value"], 10.0)
        self.assertEqual(response.data[1]["name"], "Product 1")
        self.assertEqual(response.data[1]["concentration_value"], 5.0)
        self.assertEqual(response.data[2]["name"], "Product 3")
        self.assertEqual(response.data[2]["concentration_value"], 1.0)

    def test_get_products_by_ingredient_no_match(self):
        new_ingredient = IngredientFactory.create(name="New Ingredient")
        url = reverse(
            "products_by_ingredient", kwargs={"ingredient_id": new_ingredient.id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)


class ProductDetailViewTest(APITestCase):

    def setUp(self):
        self.product = ProductFactory.create()
        self.ingredient1 = IngredientFactory.create(name="Ingredient1")
        self.ingredient2 = IngredientFactory.create(name="Ingredient2")

        ProductIngredientFactory.create(
            product=self.product, ingredient=self.ingredient1, concentration_value=5.0
        )
        ProductIngredientFactory.create(
            product=self.product, ingredient=self.ingredient2, concentration_value=10.0
        )

        self.url = reverse("product_detail", kwargs={"product_id": self.product.id})

    def test_get_product_detail_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.product.id)
        self.assertEqual(len(response.data["ingredients"]), 2)
        self.assertEqual(
            response.data["ingredients"][0]["ingredient"]["name"], "Ingredient1"
        )
        self.assertEqual(
            response.data["ingredients"][1]["ingredient"]["name"], "Ingredient2"
        )

    def test_get_product_detail_not_found(self):
        url = reverse("product_detail", kwargs={"product_id": 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ProductUpdateViewTest(APITestCase):

    def setUp(self):
        self.product = ProductFactory.create()
        self.url = reverse("product_update", kwargs={"product_id": self.product.id})
        self.valid_payload = {
            "name": "Updated Product Name",
            "description": "Updated description",
            "category": "Updated category",
            "sub_category": "Updated sub_category",
            "brand": BrandFactory.create().id,
            "line": LineFactory.create().id,
            "country": "Updated country",
            "ph": "7",
            "cruelty_free": True,
            "vegan": True,
        }
        self.invalid_payload = {
            "name": "",
            "description": "",
            "category": "",
            "sub_category": "",
            "brand": "",
            "line": "",
            "country": "",
            "ph": "",
            "cruelty_free": "",
            "vegan": "",
        }

    def test_update_product_success(self):
        response = self.client.put(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Product Name")
        self.assertEqual(self.product.description, "Updated description")
        self.assertEqual(self.product.category, "Updated category")
        self.assertEqual(self.product.sub_category, "Updated sub_category")
        self.assertEqual(self.product.country, "Updated country")
        self.assertEqual(self.product.ph, "7")
        self.assertEqual(self.product.cruelty_free, True)
        self.assertEqual(self.product.vegan, True)

    def test_update_product_not_found(self):
        url = reverse("product_update", kwargs={"product_id": 9999})
        response = self.client.put(url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, 404)

    def test_update_product_invalid_data(self):
        response = self.client.put(self.url, self.invalid_payload, format="json")
        self.assertEqual(response.status_code, 400)
