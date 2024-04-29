from django.db import models
from django.utils import timezone

class Category(models.Model):
   name = models.CharField(max_length=120, default=None)
   
   def __str__(self):
       return self.name
   

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, default="Product name not define")
    profile_img = models.ImageField()
    description = models.TextField()
    product_count = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not available'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, default="Product name not define")
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    description = models.TextField()
    display_image = models.ImageField()
    detail_image = models.ImageField()
    rating = models.FloatField(default=0.0) 
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=13,
        choices=STATUS_CHOICES,
        default='available',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name + str(self.brand) + str(self.category)
