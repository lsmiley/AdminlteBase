from django.contrib import admin
from .models import Order, OrderItem, OrderManager


admin.site.register(Order)

admin.site.register(OrderItem)


