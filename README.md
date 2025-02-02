# django_utils

Algumas utilidades para meus projetos Django

```shell
pip install --index-url https://pypi.stefanello.cc/simple/ django-utils
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
