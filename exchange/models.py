from django.db import models
from django.utils.text import slugify

from accounts.models import User


class ExchangeItem(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = 'available', 'Доступно'
        EXCHANGED = 'exchanged', 'Обменяно'
        RESERVED = 'reserved', 'Зарезервировано'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='items')
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.AVAILABLE)
    image = models.ImageField(
        upload_to="exchange_items/",
        blank=True, null=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
