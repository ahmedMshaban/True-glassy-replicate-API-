from django.shortcuts import render, redirect
from .forms import ProductForm, ProductIngredientFormSet


def index(request):
    response = "Hello, Django!"
    return render(request, "index.html", {"message": response})


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        formset = ProductIngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            ingredients = formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.product = product
                ingredient.save()
            return redirect("/")
        else:
            return render(
                request, "create_product.html", {"form": form, "formset": formset}
            )
    else:
        form = ProductForm()
        formset = ProductIngredientFormSet()

    return render(request, "create_product.html", {"form": form, "formset": formset})
