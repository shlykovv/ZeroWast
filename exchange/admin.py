from django.contrib import admin

from exchange.models import ExchangeItem, Category


admin.site.register(ExchangeItem)
admin.site.register(Category)
