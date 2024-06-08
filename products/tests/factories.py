import factory
from factory.django import DjangoModelFactory
from products.models import Brand, Line, Ingredient, Product, ProductIngredient


class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("company")


class LineFactory(DjangoModelFactory):
    class Meta:
        model = Line

    name = factory.Faker("company")


class IngredientFactory(DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = factory.Faker("word")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    description = factory.Faker("text")
    category = factory.Faker("word")
    sub_category = factory.Faker("word")
    brand = factory.SubFactory(BrandFactory)
    line = factory.SubFactory(LineFactory)
    country = factory.Faker("country")
    ph = factory.Faker("random_number", digits=2, fix_len=True)
    cruelty_free = factory.Faker("boolean")
    vegan = factory.Faker("boolean")


class ProductIngredientFactory(DjangoModelFactory):
    class Meta:
        model = ProductIngredient

    product = factory.SubFactory(ProductFactory)
    ingredient = factory.SubFactory(IngredientFactory)
    order = factory.Faker("random_digit")
    concentration_value = factory.Faker("pyfloat", positive=True)
    concentration_unit = factory.Faker("word")
