from django.urls import path

from .views import add_to_cart, cart_view, delete_item

urlpatterns = [
    path("add-to-cart/<int:item_id>", add_to_cart, name="add-to-cart"),
    path("order-summary/", cart_view, name="cart-view"),
    path("delete/<int:item_id>", delete_item, name="delete-item"),
]
