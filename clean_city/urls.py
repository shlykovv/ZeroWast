from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('exchange/', include('exchange.urls')),
    path('api/greenpoints/', include('greenpoints.urls')),
    path('api/accounts/', include('accounts.urls')),
    path(
        'about/',
        TemplateView.as_view(template_name='main/about.html'),
        name='about')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
