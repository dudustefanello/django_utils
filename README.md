# django_utils

Algumas utilidades para meus projetos Django

```shell
pip install -U --index-url https://pypi.stefanello.cc/simple/ django-utils
```

## Health Check

Implementa uma view para retornar status 200 para verificar se o sistema está online.

Pra utilizar no docker:

```yml
  healthcheck:
    test: ["CMD-SHELL", "curl -f http://localhost:8000/health/ || exit 1"]
    interval: 30s
    timeout: 10s
    retries: 3
```

## Models

Implementa classes base para models:

- **BaseModel**: Com data de criação e alteração e definição de classe Meta

## Protect Media

Implementa uma view para redirecionar para uma `internal` `location` do Nginx com o header `X-Accel-Redirect` para `/protected/`

```py
urlpatterns = [
  path('media/<path:path>/', protected_serve, {'document_root': settings.MEDIA_ROOT}),
]
```

```nginx
location /protected/ {
  internal;
  alias /path/para/mediafiles/;
}
```
