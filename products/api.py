from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Product, ProductIngredient
from .serializers import (
    ProductSerializer,
    IngredientCountSerializer,
    ProductWithConcentrationSerializer,
)


class CrueltyFreeVeganProductsView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all products from a specific brand and line that are cruelty-free and vegan",
        manual_parameters=[
            openapi.Parameter(
                "brand_id",
                openapi.IN_PATH,
                description="ID of the brand",
                type=openapi.TYPE_INTEGER,
                example=609,
            ),
            openapi.Parameter(
                "line_id",
                openapi.IN_PATH,
                description="ID of the line",
                type=openapi.TYPE_INTEGER,
                example=1463,
            ),
        ],
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, request, brand_id, line_id):
        try:
            products = Product.objects.filter(
                brand_id=brand_id, line_id=line_id, cruelty_free=True, vegan=True
            )
            if not products.exists():
                return Response(
                    {"error": "No products found matching the criteria"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CommonIngredientsView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve the most common ingredients used in products from a specific country",
        manual_parameters=[
            openapi.Parameter(
                "country",
                openapi.IN_PATH,
                description="Country code (e.g., 'KR' for South Korea)",
                type=openapi.TYPE_STRING,
                example="KR",
            ),
        ],
        responses={200: IngredientCountSerializer(many=True)},
    )
    def get(self, request, country):
        try:
            ingredients = (
                ProductIngredient.objects.filter(product__country=country)
                .values("ingredient__name")
                .annotate(count=Count("ingredient"))
                .order_by("-count")
            )
            serializer = IngredientCountSerializer(ingredients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProductsByIngredientView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all products containing a specific ingredient, sorted by the concentration of that ingredient in descending order",
        manual_parameters=[
            openapi.Parameter(
                "ingredient_id",
                openapi.IN_PATH,
                description="ID of the ingredient",
                type=openapi.TYPE_INTEGER,
                example=15096,
            ),
        ],
        responses={200: ProductWithConcentrationSerializer(many=True)},
    )
    def get(self, request, ingredient_id):
        try:
            product_ingredients = (
                ProductIngredient.objects.filter(ingredient_id=ingredient_id)
                .order_by("-concentration_value")
                .select_related("product")
            )

            products = [
                {
                    "id": pi.product.id,
                    "name": pi.product.name,
                    "description": pi.product.description,
                    "category": pi.product.category,
                    "sub_category": pi.product.sub_category,
                    "brand": pi.product.brand,
                    "line": pi.product.line,
                    "country": pi.product.country,
                    "ph": pi.product.ph,
                    "cruelty_free": pi.product.cruelty_free,
                    "vegan": pi.product.vegan,
                    "concentration_value": pi.concentration_value,
                }
                for pi in product_ingredients
            ]

            serializer = ProductWithConcentrationSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
