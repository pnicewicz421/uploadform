from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import index_view

# Create your tests here.
class index_viewTest(TestCase):
    
    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index_view)
        
    def test_index_view_returns_correct_html(self):
        request = HttpRequest()
        response = index_view(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Issue Tracker</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        