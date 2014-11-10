from django.test import TestCase
from django.core.urlresolvers import reverse

class BehavuiTest(TestCase):

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
