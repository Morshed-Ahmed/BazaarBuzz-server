from django.db import models
from categories.models import TopCategory,SubCategory

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    top_category = models.ForeignKey(TopCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images', null=True, blank=True)

    def __str__(self):
        return self.name
