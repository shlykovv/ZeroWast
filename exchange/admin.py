from django.contrib import admin
from django.utils.html import mark_safe

from exchange.models import ExchangeItem, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ExchangeItem)
class ExchangeItemAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'status',
        'location', 'created_at')


    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" wirth="80"/>')
        return '-Пусто-'
