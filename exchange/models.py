from django.db import models

from accounts.models import User


ITEM_CATEGORIES = [
    ("clothes", "Одежда"),
    ("books", "Книги"),
    ("tech", "Техника"),
    ("furniture", "Мебель"),
    ("kids", "Детские вещи"),
]


class ExchangeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=ITEM_CATEGORIES)
    image = models.ImageField(upload_to="exchange_items/", blank=True, null=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
