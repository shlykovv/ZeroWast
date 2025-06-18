from rest_framework import serializers

from greenpoints.models import GreenPoint


class GreenPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenPoint
        fields = '__all__'
        read_only_fileds = ('created_by', 'created_at',)
