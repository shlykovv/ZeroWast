from django.urls import path, include
from rest_framework.routers import DefaultRouter

from greenpoints.views import GreenPointViewSet


router = DefaultRouter()
router.register(r'points', GreenPointViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
