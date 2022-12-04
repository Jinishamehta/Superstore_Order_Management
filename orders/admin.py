from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(mm_customer)
admin.site.register(mm_order)
admin.site.register(mm_shipping_details)
