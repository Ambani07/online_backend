from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
