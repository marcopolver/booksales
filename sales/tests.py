from django.test import TestCase

# Create your tests here.
class HomeViewTest(TestCase):

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home_page.html')

