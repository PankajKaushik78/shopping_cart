from django.shortcuts import render

from .models import Product


def product_list_view(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }

    return render(request, "products/product_list.html", context)
