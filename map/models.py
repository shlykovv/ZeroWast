from django.db import models

ECO_CATEGORIES = [
    ("recycle", "Переработка"),
    ("repair", "Ремонт"),
    ("bulk", "На развес"),
    ("refill", "Заправка тары"),
]


class EcoPoint(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=ECO_CATEGORIES)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to="eco_points/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
