import csv
import json
from django.core.management.base import BaseCommand
from products.models import Brand, Line, Ingredient, Product, ProductIngredient


class Command(BaseCommand):
    help = "Populate the Product models from one or more CSV files"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_files", nargs="+", type=str, help="The path to one or more CSV files"
        )

    def handle(self, **kwargs):
        csv_files = kwargs["csv_files"]

        for csv_file_path in csv_files:
            with open(csv_file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if not row["name"]:
                        continue

                    brand = None
                    if row["brand"]:
                        brand_name = row["brand"].strip()
                        if brand_name:
                            brand, _ = Brand.objects.get_or_create(name=brand_name)

                    line = None
                    if row["line"]:
                        line_name = row["line"].strip()
                        if line_name:
                            line, _ = Line.objects.get_or_create(name=line_name)

                    product = Product.objects.create(
                        name=row["name"],
                        description=(
                            row["description"].strip().strip('"')
                            if row["description"]
                            else None
                        ),
                        category=row["category"],
                        sub_category=row["subcategory"],
                        brand=brand,
                        line=line,
                        country=row["country"],
                        ph=row["ph"] if row["ph"] else None,
                        cruelty_free=row["crueltyFree"].strip().lower() == "true",
                        vegan=row["vegan"].strip().lower() == "true",
                    )

                    ingredients = []
                    if row["ingredients"]:
                        ingredients = json.loads(row["ingredients"].replace('""', '"'))

                    concentrations = []
                    if row["concentration"]:
                        concentrations = json.loads(
                            row["concentration"].replace('""', '"')
                        )

                    for order, ingredient_data in enumerate(ingredients, start=1):
                        ingredient_name = ingredient_data["S"]
                        ingredient, _ = Ingredient.objects.get_or_create(
                            name=ingredient_name
                        )

                        concentration_value = None
                        concentration_unit = None

                        for concentration in concentrations:
                            # The ingredient key is S because the data is taken from AWS DynamoDB
                            if concentration["S"].startswith(ingredient_name):
                                parts = concentration["S"].split(":")
                                if len(parts) == 3:
                                    concentration_unit = parts[1]
                                    concentration_value = float(parts[2])
                                break

                        # Check if the ProductIngredient already exists
                        product_ingredient, created = (
                            ProductIngredient.objects.get_or_create(
                                product=product,
                                ingredient=ingredient,
                                defaults={
                                    "order": order,
                                    "concentration_value": concentration_value,
                                    "concentration_unit": concentration_unit,
                                },
                            )
                        )

                        if not created:
                            # Update the existing ProductIngredient if necessary
                            product_ingredient.order = order
                            product_ingredient.concentration_value = concentration_value
                            product_ingredient.concentration_unit = concentration_unit
                            product_ingredient.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully populated products from {csv_file_path}"
                )
            )
