from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    icon = models.CharField(max_length=100, blank=True, help_text="CSS-класс иконки или название изображения")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
