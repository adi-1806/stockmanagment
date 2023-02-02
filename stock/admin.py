from django.contrib import admin

# Register your models here.

from .models import motor_products, other_products

admin.site.register(other_products)
admin.site.register(motor_products)
