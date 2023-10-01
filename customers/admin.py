from django.contrib import admin

from core.admin import BaseAdmin
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    """Способ отображения поста в админке."""

    list_display = (
        'pk',
        'email',
    )
    search_fields = ('email',)
