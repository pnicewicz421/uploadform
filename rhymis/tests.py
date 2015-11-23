from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
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
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)
        
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'<title>Issue Tracker</title>', response.content)
        #self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_index_view_processes_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        notesText = '''
        Grazyna came crying after her cajun-style grilled cheese sandwich 
        with red peppers and stuffed portabello mushroom turned out slightly
        burnt. New grilled cheese was issued. Issue resolved.
        '''
        request.POST['notes_text'] = notesText 
        response = index_view(request)
        self.assertIn(notesText, response.content.decode())
        
        expected_html = render_to_string(
            'index.html', 
            {'notes_text': notesText}
        )
        self.assertEqual(response.content.decode(), expected_html)
        
        