import os
from uuid import uuid4
from datetime import date
from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files.base import ContentFile
from django.conf import settings


def greenpoint_photo_path(instance, filename: str):
    ext = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{ext}'
    return os.path.join(
        'greenpoints',
        instance.point_type,
        str(date.today()),
        filename
    )


class GreenPoint(models.Model):
    TYPE_CHOICES = [
        ('recycle', 'Пункт приёма'),
        ('repair', 'Ремонт'),
        ('refill', 'Заправка тары'),
        ('shop', 'Безупаковочный магазин'),
        ('other', 'Другое')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    point_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    schedule = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to=greenpoint_photo_path,
        blank=True,
        null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            output = BytesIO()
            img.thumbnail((1024, 1024))
            img.save(output, format='JPEG', quality=70) # Качесто image 70%
            output.seek(0)
            
            self.photo = ContentFile(output.read(), self.photo.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
