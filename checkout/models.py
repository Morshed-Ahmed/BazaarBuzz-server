from django.db import models


class CheckoutInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

class Payment(models.Model):
    email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    product_ids = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20) 

        
    def __str__(self):
        return f"Payment by {self.email} on {self.date}"