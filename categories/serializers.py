from rest_framework import serializers
from .models import TopCategory, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    top_category_name = serializers.CharField(source='top_category.name', read_only=True)
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'top_category', 'top_category_name']

class TopCategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = TopCategory
        fields = ['id', 'name', 'image', 'subcategories']
