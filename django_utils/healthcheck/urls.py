from django_utils.healthcheck.views import health_check
from django.urls import path


app_name = 'django_utils.healthcheck'

urlpatterns = [
    path('', health_check),
]