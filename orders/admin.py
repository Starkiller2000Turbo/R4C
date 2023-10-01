from django.contrib import admin

from core.admin import BaseAdmin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    """Способ отображения поста в админке."""

    list_display = (
        'pk',
        'customer',
        'robot_serial',
    )
    search_fields = ('email',)
