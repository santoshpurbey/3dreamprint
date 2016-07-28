from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("category", "name", "slug", "image", "description",
                  "price", "stock", "available", "created", "updated")
