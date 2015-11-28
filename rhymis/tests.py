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
        
        print (expected_html)
        print ()
        print (response.content.decode())
        
        self.assertEqual(response.content.decode(), expected_html)
        
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'<title>Issue Tracker</title>', response.content)
        #self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_index_view_does_not_save_blank_entries(self):
        request = HttpRequest()
        index_view(request)
        self.assertEqual(Record.objects.count(), 0)
        

    
    def prep_POST_request(self):
        gmt5 = GMT5()
        
        request = HttpRequest()
        request.method = 'POST'
        
        datetimeText = datetime.datetime(2015, 11, 21, 14, 37, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        request.POST['date_time_text'] = str(datetimeText)
        request.POST['location_text'] = locationText
        request.POST['youth_name_text'] = youthNameText
        request.POST['notes_text'] = notesText 
        
        response = index_view(request)
        return response

        
    def test_index_view_processes_POST_request(self):
        #Check to make sure POST request saved in database
        self.prep_POST_request()
        
        gmt5 = GMT5()
        datetimeText = datetime.datetime(2015, 11, 21, 14, 37, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        self.assertEqual(Record.objects.count(), 1)
        new_record = Record.objects.first()
        self.assertEqual(new_record.datetimeText, datetimeText)
        self.assertEqual(new_record.locationText, locationText)
        self.assertEqual(new_record.youthNameText, youthNameText)
        self.assertEqual(new_record.notesText, notesText)
    
    def test_index_view_redirects_after_POST_request(self):        
        response = self.prep_POST_request()
        
        self.assertEqual(response.status_code, 302) #check for redirect
        self.assertEqual(response['location'], '/')
        
        ###
        #self.assertIn(notesText, response.content.decode())
        #self.assertIn(str(datetimeText), response.content.decode())
        #self.assertIn(locationText, response.content.decode())
        #self.assertIn(youthNameText, response.content.decode())
        
        #expected_html = render_to_string(
        #    'index.html', 
        #    {'date_time_text': str(datetimeText),
        #    'location_text': locationText,
        #    'youth_name_text': youthNameText,
        #    'notes_text': notesText}
        #)
        
        #self.assertEqual(response.content.decode(), expected_html)
        ###
        
    def test_index_view_with_multiple_items(self):
        gmt5 = GMT5()
    
        locationText1 = 'Home'
        locationText2 = 'Washington'
        
        Record.objects.create(datetimeText=datetime.datetime(2015, 1, 23, 4, 56, tzinfo=gmt5), locationText='Home', youthNameText='Monty Python', notesText='The notes are here')
        Record.objects.create(datetimeText=datetime.datetime(2016, 11, 15, 23, 1, tzinfo=gmt5), locationText='Washington', youthNameText='White House', notesText='Bad News')
        
        request = HttpRequest()
        response = index_view(request)
        
        print (response.content.decode())
        
        self.assertIn(locationText1, response.content.decode())
        self.assertIn(locationText2, response.content.decode())
        
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