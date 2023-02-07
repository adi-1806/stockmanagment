from django.contrib import admin

# Register your models here.

from .models import selled_motor, selled_other

admin.site.register(selled_motor)
admin.site.register(selled_other)