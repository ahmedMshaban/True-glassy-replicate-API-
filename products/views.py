from django.shortcuts import render


def index(request):
    response = "Hello, Django!"
    return render(request, "index.html", {"message": response})
