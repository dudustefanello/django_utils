from django_utils.healthcheck.views import health_check
from django.urls import path


app_name = 'agenda'

urlpatterns = [
    path('', health_check),
]