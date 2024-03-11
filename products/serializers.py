from rest_framework import serializers
from .models import Product,ProductReview

class ProductSerializer(serializers.ModelSerializer):
    top_category = serializers.StringRelatedField(many=False)
    sub_category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'top_category', 'sub_category', 'image']

class ProductReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = ProductReview
        fields = ['id', 'product', 'username','user', 'review_text', 'rating', 'created_at']

    def get_username(self, obj):
        return obj.user.username