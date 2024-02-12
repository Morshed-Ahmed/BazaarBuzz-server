from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    top_category = serializers.StringRelatedField(many=False)
    sub_category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'top_category', 'sub_category', 'image']
