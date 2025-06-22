from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'main/home.html')),
    path('api/exchange/', include('exchange.urls')),
    path('api/greenpoints/', include('greenpoints.urls')),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh')
]
