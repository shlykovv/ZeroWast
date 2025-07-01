from rest_framework import serializers

from exchange.models import ExchangeItem


class ExchangeItemSerializer(serializers.ModelSerializer):
    # Возвращаем имя через метод __str__
    category = serializers.StringRelatedField()

    class Meta:
        model = ExchangeItem
        fields = '__all__'
