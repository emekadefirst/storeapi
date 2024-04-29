from django.contrib.auth.models import User
from django.db import models
from api.order.models import Order




class Payment(models.Model):
    class TRANSACTION_STATUS(models.TextChoices):
        SUCCESSFUL = "SUCCESSFUL", "Successful"
        PENDING = "PENDING", "Pending"
        FAILED = "FAILED", "Failed"
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name=None)
    amount = models.FloatField(default="0.00")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, name=None)
    status = models.CharField(max_length=50, choices=TRANSACTION_STATUS.choices, default=TRANSACTION_STATUS.PENDING)
    reference =  models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"User: {self.user.email}, Product: {self.order.cart.product.name}, Cost: {self.order.cart.cost}"

    class Meta:
        ordering = ["-time"]  # Ordering by the 'time' field in descending order

