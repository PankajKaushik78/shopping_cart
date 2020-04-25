from django.db import models
from datetime import datetime

from products.models import Product
from profiles.models import Profile


class OrderItem(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=datetime.now)
    date_ordered = models.DateTimeField(null=True)

    def _str__(self):
        return self.product.title


class Order(models.Model):
    ref_code = models.CharField(max_length=15, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return self.owner
