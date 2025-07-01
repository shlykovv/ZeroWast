from django.db import models


class EcoChallenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    points = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
