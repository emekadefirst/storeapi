from rest_framework import serializers
from .model import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        cart = Cart.objects.create(
            user=validated_data['user'],
            product=validated_data['product'],
            quantity=validated_data['quantity']
        )
        return cart

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
