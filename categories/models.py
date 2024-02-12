from django.db import models

# Create your models here.
class TopCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/images', null=True, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    top_category = models.ForeignKey(TopCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name