from rest_framework import serializers

from .models import Product, Brand, Line, ProductIngredient, Ingredient


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ["id", "name"]


class IngredientCountSerializer(serializers.Serializer):
    ingredient__name = serializers.CharField(max_length=255)
    count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    line = LineSerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "sub_category",
            "brand",
            "line",
            "country",
            "ph",
            "cruelty_free",
            "vegan",
            "ingredients",
        ]


class ProductWithConcentrationSerializer(serializers.ModelSerializer):
    concentration_value = serializers.FloatField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "sub_category",
            "brand",
            "line",
            "country",
            "ph",
            "cruelty_free",
            "vegan",
            "concentration_value",
        ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class ProductIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = ProductIngredient
        fields = ["ingredient", "order", "concentration_value", "concentration_unit"]


class ProductDetailSerializer(serializers.ModelSerializer):
    ingredients = ProductIngredientSerializer(source="productingredient_set", many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "sub_category",
            "brand",
            "line",
            "country",
            "ph",
            "cruelty_free",
            "vegan",
            "ingredients",
        ]


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "sub_category",
            "brand",
            "line",
            "country",
            "ph",
            "cruelty_free",
            "vegan",
        ]
