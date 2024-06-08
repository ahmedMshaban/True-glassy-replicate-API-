from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Product, ProductIngredient


class ProductForm(ModelForm):
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

    def clean(self):
        cleaned_data = super().clean()
        ph = cleaned_data.get("ph")

        if ph:
            try:
                ph_value = float(ph)
                if ph_value < 0 or ph_value > 14:
                    raise forms.ValidationError("pH must be between 0 and 14.")
            except ValueError:
                raise forms.ValidationError("pH must be a numeric value.")

        return cleaned_data


class ProductIngredientForm(ModelForm):
    class Meta:
        model = ProductIngredient
        fields = ["ingredient", "order", "concentration_value", "concentration_unit"]

    def clean(self):
        cleaned_data = super().clean()
        concentration_value = cleaned_data.get("concentration_value")

        if concentration_value is not None and concentration_value <= 0:
            raise forms.ValidationError("Concentration value must be positive.")

        return cleaned_data


ProductIngredientFormSet = inlineformset_factory(
    Product, ProductIngredient, form=ProductIngredientForm, extra=1, can_delete=True
)
