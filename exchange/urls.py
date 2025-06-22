from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exchange.views import ExchangeItemViewSet, exchange_list


router = DefaultRouter()
router.register(r'items', ExchangeItemViewSet)


urlpatterns = [
    path('', exchange_list, name='exchange_list'),
    path('api/', include(router.urls)),
]
