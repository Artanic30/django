from django.test import TestCase
from .models import Site, User
# Create your tests here.


class SiteModelTests(TestCase):
    def setUp(self):
        User.objects.create(name='test1', email='t1@edu.cn', is_active=True, first_name='test1', username='test1')
        print(User.objects.all())
        response = self.client.get('/api/site')
        print(response)

    def test_get_site(self):
        user = User.objects.get(name='test1')
        response = self.client.get('/api/site')
        print(response, user)

    def test_post_site(self):
        response = self.client.post('/api/site', {'location': 'test1'})
        print(response)
