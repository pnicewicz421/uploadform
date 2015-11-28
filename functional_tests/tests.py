from selenium import webdriver
from django.test import LiveServerTestCase

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
        

    def test_right_title(self):
        #Of course, let's make sure that Issue Tracker appears in the title.
        self.browser.get(self.live_server_url)
        self.assertIn('Issue Tracker', self.browser.title)
        
        #Then, we will make sure that there's a header with that information
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My Issue Tracker', header_text)
        
        #She sees a table with headers labeled: 
        table = self.browser.find_element_by_id('id_table')
        headers = table.find_elements_by_tag_name('th')
        
        #   - Date (date field)
        #   - Time (date field)
        #   - Location (text field; 50 chars max)
        #   - Youth Name (text field; 50 chars max)
        #   - Notes (text field; 500 chars max)
        self.assertTrue(any(header.text == 'Date' for header in headers))
        self.assertTrue(any(header.text == 'Location' for header in headers))
        self.assertTrue(any(header.text == 'Youth Name' for header in headers))
        self.assertTrue(any(header.text == 'Notes' for header in headers))
        
        #She also sees blank fields below the header ready to populate the table
        inputDateTime = self.browser.find_element_by_id('id_date_time')
        inputLocation = self.browser.find_element_by_id('id_location')
        inputYouthName = self.browser.find_element_by_id('id_youth_name')
        inputNotes = self.browser.find_element_by_id('id_notes')
        
        submitButton = self.browser.find_element_by_id('id_submit')
        
        
        gmt5 = GMT5()
        
        # She types in her first case:
        #   - Date: 11/21/2015
        #   - Time: 2:37 PM EST
        #   - Location: Woodberry Park
        #   - Youth Name: Grazyna Kwiatkowska
        #   - Notes: Grazyna came crying after her cajun-style grilled cheese sandwich
        #   - with red peppers and stuffed portabello mushrooms turned out 
        #   - slightly burnt. New grilled cheese was issued. Issue resolved.'
        dateTimeText = datetime.datetime(2015, 11, 21, 15, 21, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        row_text = [str(dateTimeText), locationText, youthNameText, notesText]
        
       # Grazyna came crying after her cajun-style grilled cheese sandwich 
        #with red peppers and stuffed portabello mushroom turned out slightly
        #burnt. New grilled cheese was issued. Issue resolved.
        #'''
        
        # Convert to this format 'Nov. 21, 2015, 10:21 a.m.'

        inputDateTime.send_keys(str(dateTimeText))
        inputLocation.send_keys(locationText)
        inputYouthName.send_keys(youthNameText)
        inputNotes.send_keys(notesText)

        # For now she types in enter in the notes box to send the information
        # Later, there will be a submit button once we get to forms

        submitButton.click()
        
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/records/.+', 'Actual url was %s' % user1_list_url)
        
        time.sleep(1)

        #The first case now appears in the table
        # Test to make sure info was submitted 
        self.check_for_row_in_table(row_text)
        
        #Second user comes along
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        self.browser.get(self.browser.live_server_url)
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn(locationText, body_text)
        self.assertNotIn(youthNameText, body_text)
        self.assertNotIn(notesText, body_text)
        
        dateTimeText = datetime.datetime(2013, 5, 4, 14, 21, tzinfo=gmt5)
        locationText = 'OLQP'
        youthNameText = 'Emilka and Przemek'
        notesText = 'Most beautiful day ever'
        
        row_text = [str(dateTimeText), locationText, youthNameText, notesText]
        
       # Grazyna came crying after her cajun-style grilled cheese sandwich 
        #with red peppers and stuffed portabello mushroom turned out slightly
        #burnt. New grilled cheese was issued. Issue resolved.
        #'''
        
        # Convert to this format 'Nov. 21, 2015, 10:21 a.m.'

        inputDateTime.send_keys(str(dateTimeText))
        inputLocation.send_keys(locationText)
        inputYouthName.send_keys(youthNameText)
        inputNotes.send_keys(notesText)

        # For now she types in enter in the notes box to send the information
        # Later, there will be a submit button once we get to forms

        submitButton.click()
        
        self.check_for_row_in_table(row_text)
        
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, '/records/.+', 'Actual url was %s' % user2_list_url)
        self.assertNotEqual(user2_list_url, user1_list_url)
        
        self.fail('Finish the test')
        
#Done for now
class GMT5(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5)
    def dst(self, dt):
        return datetime.timedelta(0)