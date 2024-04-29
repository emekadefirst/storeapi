from django.contrib import admin
from api.cart.model import Cart
from api.order.models import Order
from api.product.model import Product, Category, Brand
from api.payment.model import Payment
from django.contrib.auth.models import User


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'cost']
    search_fields = ['user__username', 'product__name']
    list_filter = ['user']

admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart', 'status']
    search_fields = ['cart__user__username']
    list_filter = ['status']

admin.site.register(Order, OrderAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'order', 'status', 'reference', 'time']
    search_fields = ['user__email', 'order__cart__product__name']
    list_filter = ['status']

admin.site.register(Payment, PaymentAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_count']
    search_fields = ['name']
    list_filter = ['product_count']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'quantity', 'status', 'created_at']
    search_fields = ['name', 'brand__name', 'category__name']
    list_filter = ['status', 'created_at']



