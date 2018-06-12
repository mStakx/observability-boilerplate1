from django.contrib import admin
from server.models import Pizza, Order

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'cost')
    search_fields = ('name', 'size', 'cost')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'cost')
    search_fields = ('order_id', 'cost')
