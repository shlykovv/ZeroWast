# Generated by Django 5.2.3 on 2025-06-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EcoPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('recycle', 'Переработка'), ('repair', 'Ремонт'), ('bulk', 'На развес'), ('refill', 'Заправка тары')], max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('schedule', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='eco_points/')),
            ],
        ),
    ]
