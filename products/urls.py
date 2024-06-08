from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views
from .api import (
    CrueltyFreeVeganProductsView,
    CommonIngredientsView,
    ProductsByIngredientView,
    ProductDetailView,
    ProductUpdateView,
    ProductCreateView,
    DeleteUnbrandedUnveganProductsView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="True Glassy API",
        default_version="v1",
        description="Skin care products API",
        contact=openapi.Contact(email="ahmed.ms.elias@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", views.index, name="index"),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path(
        "api/products/brand/<int:brand_id>/line/<int:line_id>/cruelty_free_vegan/",
        CrueltyFreeVeganProductsView.as_view(),
        name="cruelty_free_vegan_products",
    ),
    path(
        "api/products/country/<str:country>/common_ingredients/",
        CommonIngredientsView.as_view(),
        name="common_ingredients",
    ),
    path(
        "api/products/ingredient/<int:ingredient_id>/sorted_by_concentration/",
        ProductsByIngredientView.as_view(),
        name="products_by_ingredient",
    ),
    path(
        "api/product/<int:product_id>/details/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "api/product/<int:product_id>/update/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path("api/products/add/", ProductCreateView.as_view(), name="product_add"),
    path(
        "api/products/unbranded_unvegan/",
        DeleteUnbrandedUnveganProductsView.as_view(),
        name="delete_unbranded_unvegan_products",
    ),
    path("create_product/", views.create_product, name="create_product"),
]
