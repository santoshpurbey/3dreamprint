from rest_framework import serializers

from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'image', 'description', 'price',
                'stock', 'available', 'updated', 'created',)
