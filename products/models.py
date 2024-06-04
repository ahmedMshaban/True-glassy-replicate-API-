from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subcategories",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("name", "parent_category")

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Attributes(models.Model):
    ph = models.FloatField(null=True, blank=True)
    crueltyFree = models.BooleanField()
    vegan = models.BooleanField()

    def __str__(self):
        return f"Attributes: pH={self.ph}, CrueltyFree={self.crueltyFree}, Vegan={self.vegan}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    marketed = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient", through="ingredients.ProductIngredient"
    )

    def __str__(self):
        return self.name
