from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

import datetime

from rhymis.models import Record, RecordNumber

from .views import index_view

# Create your tests here.
class newrecordTest(TestCase):
    def test_new_record_template_loads_correctly(self):
        tablenumbers = RecordNumber.objects.count()
        
        response = self.client.get('/records/new')
        self.assertTemplateUsed(response, 'newtable.html')
        
        self.assertEqual(tablenumbers + 1, RecordNumber.objects.count())
        tablenumbers += 1
    
    def test_add_a_new_record_to_a_new_table(self):
        #let's try adding multiple records
        tablenumber = RecordNumber.objects.create()
        
        gmt5 = GMT5()
        datetimeText = '05/04/2013'
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        self.client.post('/records/%d/add_record' % tablenumber.id, data=
        {'date_time_text': datetimeText, 'location_text': locationText, 
        'youth_name_text': youthNameText, 'notes_text': notesText})
    
        self.assertEqual(Record.objects.count(), 1)
        new_record = Record.objects.first()
        self.assertEqual(new_record.datetimeText, datetimeText)
        self.assertEqual(new_record.locationText, locationText)
        self.assertEqual(new_record.youthNameText, youthNameText)
        self.assertEqual(new_record.notesText, notesText)

        datetimeText = '07/18/2015'
        locationText = 'Asd'
        youthNameText = 'Name'
        notesText = 'Just writing some notes here'
        
        self.client.post('/records/%d/add_record' % tablenumber.id, data=
        {'date_time_text': datetimeText, 'location_text': locationText, 
        'youth_name_text': youthNameText, 'notes_text': notesText})
    
        self.assertEqual(Record.objects.count(), 2)
        new_record = Record.objects.get(id=2)
        self.assertEqual(new_record.datetimeText, datetimeText)
        self.assertEqual(new_record.locationText, locationText)
        self.assertEqual(new_record.youthNameText, youthNameText)
        self.assertEqual(new_record.notesText, notesText)
        
        
        
class GMT5(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5)
    def dst(self, dt):
        return datetime.timedelta(0)              
        
        


