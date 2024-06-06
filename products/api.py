from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema


class CrueltyFreeVeganProductsView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all products from a specific brand and line that are cruelty-free and vegan",
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, brand_id, line_id):
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
