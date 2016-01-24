from selenium import webdriver
from django.test import LiveServerTestCase
from rhymis.models import Record, RecordNumber

#from selenium.webdriver.common.keys import Keys

import unittest
import time
import datetime

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_table(self, row_text):
        #Since I don't want to keep writing out the variables
        #names every time, row_text will be a list of variable items
        
        dateTimeText = row_text[0]
        locationText = row_text[1]
        youthNameText = row_text[2]
        notesText = row_text[3]
        
        table = self.browser.find_element_by_id('id_table')
        rows = table.find_elements_by_tag_name('td')

        #self.assertEqual(time.strftime(dateTimeText, '%Y-%m-%dT%H:%M:%S'), time.strptime(rows[0].text, '%Y-%m-%dT%H:%M:%S'))
        self.assertIn(locationText, [row.text for row in rows])
        self.assertIn(youthNameText, [row.text for row in rows])
        self.assertIn(notesText, [row.text for row in rows])
        
    def test_make_sure_home_page_lists_links_to_all_of_the_records(self):
        #Of course, let's make sure that Issue Tracker appears in the title.
        self.browser.get(self.live_server_url)
        self.assertIn('Issue Tracker', self.browser.title)
        
        #Then, we will make sure that there's a header with that information
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Pick a Record', header_text)
        
        #Major reworking of the site.
        #I want to see a list of all the tables (records) with hyperlinks
        #to each one.
        
        #start out with 0 ?
        numbers_record = RecordNumber.objects.count()
        if numbers_record != 0:
            #List a url with the count
            for i in range(numbers_record) + 1:
                bullets = self.browser.find_elements_by_tag_name('ul')
                self.assertTrue(any(bullet.text == str(i) for bullet in bullets))
            else:
                self.assertEqual(numbers_record, 0)
        
        #now click on each one
        #implement later
        links = self.browser.find_elements_by_tag_name('a')
        
        
        #click to do a new record
        self.assertTrue(any(link.text == 'New Table' for link in links))
        self.browser.find_element_by_id('new_table').click()
        
        #make sure you are in the new record page
        current_url = self.browser.current_url
        self.assertIn('/records/new', current_url)
        
        #make sure the record number is included in the heading
        heading = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(str(numbers_record + 1), heading)
        
        #now submit a record in the table and see what happens
        inputDateTime = self.browser.find_element_by_id('id_date_time')
        inputLocation = self.browser.find_element_by_id('id_location')
        inputYouthName = self.browser.find_element_by_id('id_youth_name')
        inputNotes = self.browser.find_element_by_id('id_notes')
        
        submitButton = self.browser.find_element_by_id('id_submit')
        
        gmt5 = GMT5()
        
        dateTimeText = datetime.datetime(2015, 11, 21, 15, 21, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        row_text = [str(dateTimeText), locationText, youthNameText, notesText]
        
        inputDateTime.send_keys(str(dateTimeText))
        inputLocation.send_keys(locationText)
        inputYouthName.send_keys(youthNameText)
        inputNotes.send_keys(notesText)
        
        submitButton.click()
        
        #ok, we've sent the first record. now, verify that record is up and running
        records = self.browser.find_elements_by_id('td')
        self.assertTrue(any(record.text == locationText) for record in records)
        self.assertTrue(any(record.text == youthNameText) for record in records)
        self.assertTrue(any(record.text == notesText) for record in records)
        self.assertTrue(any(record.text == dateTimeText) for record in records)
        
        inputDateTime = self.browser.find_element_by_id('id_date_time')
        inputLocation = self.browser.find_element_by_id('id_location')
        inputYouthName = self.browser.find_element_by_id('id_youth_name')
        inputNotes = self.browser.find_element_by_id('id_notes')
        
        submitButton = self.browser.find_element_by_id('id_submit')
        
        
        datetimeText = datetime.datetime(2016, 1, 18, 12, 00, tzinfo=gmt5)
        locationText = 'Asd'
        youthNameText = 'Name'
        notesText = 'Just writing some notes here'
        
        inputDateTime.send_keys(str(dateTimeText))
        inputLocation.send_keys(locationText)
        inputYouthName.send_keys(youthNameText)
        inputNotes.send_keys(notesText)
        
        submitButton.click()
        
        records = self.browser.find_elements_by_id('td')
        self.assertTrue(any(record.text == locationText) for record in records)
        self.assertTrue(any(record.text == youthNameText) for record in records)
        self.assertTrue(any(record.text == notesText) for record in records)
        self.assertTrue(any(record.text == dateTimeText) for record in records)
        
class GMT5(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5)
    def dst(self, dt):
        return datetime.timedelta(0)        
                
        
        
        #She sees a table with headers labeled: 
        # self.assertEqual(self.live_server_url, self.webdriver.getCurrentUrl())
    
       
      