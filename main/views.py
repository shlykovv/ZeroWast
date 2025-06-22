import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from exchange.models import ExchangeItem
from greenpoints.models import GreenPoint


def home_page(request):
    items = ExchangeItem.objects.filter(is_active=True)[:6]
    greenpoints = GreenPoint.objects.all()
    greenpoints_json = json.dumps([
        {
            'name': point.name,
            'description': point.description,
            'lat': point.latitude,
            'lng': point.longitude
        }
        for point in greenpoints
    ], cls=DjangoJSONEncoder)

    context = {
        'items': items,
        'greenpoints_json': greenpoints_json
    }
    return render(request, 'main/home.html', context)
