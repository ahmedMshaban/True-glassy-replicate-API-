from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProductIngredient(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("ingredients.Ingredient", on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = ("product", "ingredient")

    def __str__(self):
        return f"{self.product} - {self.ingredient}"
