from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exchange.views import ExchangeItemViewSet


router = DefaultRouter()
router.register(r'exchange-items', ExchangeItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
