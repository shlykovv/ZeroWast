from django.urls import path, include
from rest_framework.routers import DefaultRouter

from greenpoints.views import GreenPointViewSet, GreenPointCreateView


router = DefaultRouter()
router.register(r'points', GreenPointViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('greenpoints/create/',
         GreenPointCreateView.as_view(),
         name='greenpoint-create')
]
