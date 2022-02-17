from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main.html')


def product_list(request):
    return render(request, "product_list.html")
