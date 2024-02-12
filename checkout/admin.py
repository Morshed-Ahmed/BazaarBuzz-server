from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CheckoutInfo)
admin.site.register(models.Payment)