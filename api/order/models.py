from django.db import models
from api.cart.model import Cart

class Order(models.Model):
    class ORDER_STATUS(models.TextChoices):
        PENDING = "PENDING", "Pending"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS.choices, default=ORDER_STATUS.PENDING
    )

    def __str__(self):
        return f"{self.cart} - {self.cart.user}"


