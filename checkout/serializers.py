from rest_framework import serializers
from .models import CheckoutInfo,Payment

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutInfo
        fields = ['full_name', 'email', 'phone_number', 'zip_code','address_1','address_2']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'