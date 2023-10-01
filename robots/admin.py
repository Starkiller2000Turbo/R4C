from django.contrib import admin

from core.admin import BaseAdmin
from robots.models import Robot


@admin.register(Robot)
class PostAdmin(BaseAdmin):
    """Способ отображения поста в админке."""

    list_display = (
        'pk',
        'serial',
        'model',
        'version',
        'created',
    )
    search_fields = ('serial',)
    list_filter = ('created',)
