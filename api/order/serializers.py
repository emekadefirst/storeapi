from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        cart = Order.objects.create(
            user=validated_data['id'],
            product=validated_data['date'],
            quantity=validated_data['venue']
        )
        return cart
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()