from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def protected_media(request, path):
    response = HttpResponse()
    response['X-Accel-Redirect'] = f'/{settings.MEDIA_ROOT}/{path}'
    return response
