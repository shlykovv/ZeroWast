from django.db import models
from django.utils.text import slugify

from accounts.models import User


class ExchangeItem(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = 'available', 'Доступно'
        EXCHANGED = 'exchanged', 'Обменяно'
        RESERVED = 'reserved', 'Зарезервировано'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='items',
        verbose_name='Категория',)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.AVAILABLE,
        verbose_name='Статус')
    image = models.ImageField(
        upload_to="exchange_items/",
        blank=True, null=True,
        verbose_name='Изображение товара')
    location = models.CharField(max_length=255, verbose_name='Местоположение')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.category.name})"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
