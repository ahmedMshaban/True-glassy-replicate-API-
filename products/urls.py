from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views
from .api import CrueltyFreeVeganProductsView, CommonIngredientsView

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
]
