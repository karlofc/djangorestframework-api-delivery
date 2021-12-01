from django.contrib import admin
from django.db import models
from orders.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size', 'order_status', 'quantity', 'created_at']
    list_filter = ['created_at', 'order_status', 'size']

admin.site.register(Order, OrderAdmin)
