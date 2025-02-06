from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model


class ProtectMediaTest(TestCase):
    path = 'arquivo.txt'
    url = f'/protect/media/{path}'
    creds = {'username': 'testuser', 'password': '12345'}

    def setUp(self):
        self.user = get_user_model().objects.create_user(**self.creds)

    def test_protect_media_login(self):
        """
        Testa se o acesso à mídia protegida redireciona para a página de login
        quando o usuário não está autenticado.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(settings.LOGIN_URL, response.url)
        self.assertIn(self.path, response.url)

    def test_protect_media_protect(self):
        """
        Testa se o acesso à mídia protegida é permitido quando o usuário está
        autenticado e se o cabeçalho 'X-Accel-Redirect' está correto.
        """
        self.client.login(**self.creds)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'{settings.MEDIA_ROOT}/{self.path}', response.headers['X-Accel-Redirect'])
