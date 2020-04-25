from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from products.models import Product
from profiles.models import Profile
from .models import OrderItem, Order


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    unordered_items = Order.objects.filter(
        owner=user_profile, is_ordered=False)
    if unordered_items.exists():
        return unordered_items[0]
    return 0


@login_required
def add_to_cart(request, **kwargs):
    profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get("item_id", "")).first()

    if product in request.user.profile.items.all():
        messages.info(request, "You already own this item")
        return redirect("product-list")

    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(
        owner=profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.save()

    messages.info(request, "Item added to cart")
    return redirect("product-list")


@login_required
def cart_view(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, "cart/cart_view.html", context)


@login_required
def delete_item(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect("cart-view")
