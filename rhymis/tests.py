from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

import datetime

from rhymis.models import Record

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
        
class GMT5(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5)
    def dst(self, dt):
        return datetime.timedelta(0)

class ModelTest(TestCase):
    
    def test_save_and_retrieve(self):
        gmt5 = GMT5()
        
        first_record = Record()
        first_record.datetimeText = datetime.datetime(2015, 11, 26, 15, 32, tzinfo=gmt5)
        #first_record.timeText = datetime.time(15, 32) #EST
        first_record.locationText = 'OT'
        first_record.youthNameText = 'Oscar Peterson'
        first_record.notesText = 'OP was the OG even before the term was coined'
        first_record.save()
        
        second_record = Record()
        second_record.datetimeText = datetime.datetime(1967, 1, 25, 3, 41, tzinfo=gmt5)
        #second_record.timeText = datetime.time(3, 41) #UTC
        second_record.locationText = 'Reykjavik'
        second_record.youthNameText = 'Olaf the Hippie'
        second_record.notesText = 'Made up viking hippie. Is that a thing'
        second_record.save()
        
        saved_items = Record.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.datetimeText, datetime.datetime(2015, 11, 26,15, 32, tzinfo=gmt5))
        self.assertEqual(first_saved_item.locationText, 'OT')
        self.assertEqual(first_saved_item.youthNameText, 'Oscar Peterson')
        self.assertEqual(first_saved_item.notesText, 'OP was the OG even before the term was coined')
        
        self.assertEqual(second_saved_item.datetimeText, datetime.datetime(1967, 1, 25, 3, 41, tzinfo=gmt5))
        self.assertEqual(second_saved_item.locationText, 'Reykjavik')
        self.assertEqual(second_saved_item.youthNameText, 'Olaf the Hippie')
        self.assertEqual(second_saved_item.notesText, 'Made up viking hippie. Is that a thing')