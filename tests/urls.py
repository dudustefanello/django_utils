from django.urls import path, include


urlpatterns = [
    path('health/', include('django_utils.healthcheck.urls')),
    path('protect/', include('django_utils.protectmedia.urls')),
]