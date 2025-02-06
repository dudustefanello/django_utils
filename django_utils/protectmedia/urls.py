from django.urls import path

from django_utils.healthcheck.views import health_check
from django_utils.protectmedia.views import protected_media


app_name = 'django_utils.protectmedia'

urlpatterns = [
    path('media/<path:path>', protected_media),
]