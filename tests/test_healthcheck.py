from django.test import TestCase


class HealthCheckTest(TestCase):

    def test_health_check(self):
        """
        Testa se o endpoint de health check retorna o status 200 e o JSON esperado.
        """
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok'})
