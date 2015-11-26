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
        
        dateText = '11/21/2015'
        timeText = '2:37 PM EST'
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        request.POST['date_text'] = dateText
        request.POST['time_text'] = timeText
        request.POST['location_text'] = locationText
        request.POST['youth_name_text'] = youthNameText
        request.POST['notes_text'] = notesText 
        response = index_view(request)
        self.assertIn(notesText, response.content.decode())
        
        expected_html = render_to_string(
            'index.html', 
            {'date_text': dateText,
            'time_text': timeText,
            'location_text': locationText,
            'youth_name_text': youthNameText,
            'notes_text': notesText}
        )
        self.assertEqual(response.content.decode(), expected_html)
        
        