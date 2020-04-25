from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title
