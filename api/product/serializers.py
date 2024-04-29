from rest_framework import serializers
from .model import Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'description', 'display_image', 'detail_image', 'rating', 'created_at', 'status', 'category_name', 'brand_name']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.description = validated_data.get('description', instance.description)
        instance.display_image = validated_data.get('display_image', instance.display_image)
        instance.detail_image = validated_data.get('detail_image', instance.detail_image)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
