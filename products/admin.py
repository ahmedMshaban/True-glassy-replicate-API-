from django.contrib import admin
from .models import Brand, Ingredient, Line, Product, ProductIngredient

admin.site.register(Brand)
admin.site.register(Ingredient)
admin.site.register(Line)
admin.site.register(Product)
admin.site.register(ProductIngredient)
