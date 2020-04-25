from django.urls import path, include

from .views import product_list_view

urlpatterns = [
    path('', product_list_view, name="product-list"),
]
