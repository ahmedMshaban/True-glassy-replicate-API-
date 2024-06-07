from rest_framework import serializers

from .models import Product, Brand, Line


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
