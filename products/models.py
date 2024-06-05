from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    line = models.ForeignKey(Line, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.CharField(max_length=255)
    ph = models.CharField(max_length=50, null=True, blank=True)
    cruelty_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    ingredients = models.ManyToManyField("Ingredient", through="ProductIngredient")

    def __str__(self):
        return self.name


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # The order of the ingredient in the product's ingredients list is important
    # Because the first ingredient is the most concentrated one and the last one is the least
    order = models.IntegerField()
    concentration_value = models.FloatField(null=True, blank=True)
    concentration_unit = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ("product", "ingredient")

    def __str__(self):
        return f"{self.product.name} (ID: {self.product.id}) - {self.ingredient.name} (ID: {self.ingredient.id})"
