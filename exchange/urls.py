from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exchange.views import ExchangeItemViewSet, exchange_list, item_detail


app_name = 'exchange'


router = DefaultRouter()
router.register(r'items', ExchangeItemViewSet)


urlpatterns = [
    path('', exchange_list, name='item_list'),
    path('item/<int:pk>', item_detail, name='item_detail'),
    path('api/', include(router.urls)),
]
