from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
    )
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"OrderNo - {self.pk}, Product_Name - {self.product_name}"