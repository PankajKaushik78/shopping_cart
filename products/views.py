from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Product
from cart.models import OrderItem, Order


@login_required
def product_list_view(request):
    product_list = Product.objects.all()
    filtered_orders = Order.objects.filter(
        owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [
            product.product for product in user_order_items]

    context = {
        'product_list': product_list,
        'current_order_products': current_order_products,
    }

    return render(request, "products/product_list.html", context)
