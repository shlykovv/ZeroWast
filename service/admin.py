from django.contrib import admin

from service.models import Service, Category


admin.site.register(Category)
admin.site.register(Service)
