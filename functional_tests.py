from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_right_title(self):
        #Of course, let's make sure that Issue Tracker appears in the title.
        self.browser.get('http://localhost:8000')
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
        self.assertTrue(any(header.text == 'Time' for header in headers))
        self.assertTrue(any(header.text == 'Location' for header in headers))
        self.assertTrue(any(header.text == 'Youth Name' for header in headers))
        self.assertTrue(any(header.text == 'Notes' for header in headers))
        
        #She also sees blank fields below the header ready to populate the table
        inputDate = self.browser.find_element_by_id('id_date')
        inputTime = self.browser.find_element_by_id('id_time')
        inputLocation = self.browser.find_element_by_id('id_location')
        inputYouthName = self.browser.find_element_by_id('id_youth_name')
        inputNotes = self.browser.find_element_by_id('id_notes')
        
        submitButton = self.browser.find_element_by_id('id_submit')
        
        # She types in her first case:
        #   - Date: 11/21/2015
        #   - Time: 2:37 PM EST
        #   - Location: Woodberry Park
        #   - Youth Name: Grazyna Kwiatkowska
        #   - Notes: Grazyna came crying after her cajun-style grilled cheese sandwich
        #   - with red peppers and stuffed portabello mushrooms turned out 
        #   - slightly burnt. New grilled cheese was issued. Issue resolved.'
        dateText = '11/21/2015'
        timeText = '2:37 PM EST'
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
       # Grazyna came crying after her cajun-style grilled cheese sandwich 
        #with red peppers and stuffed portabello mushroom turned out slightly
        #burnt. New grilled cheese was issued. Issue resolved.
        #'''
        inputDate.send_keys(dateText)
        inputTime.send_keys(timeText)
        inputLocation.send_keys(locationText)
        inputYouthName.send_keys(youthNameText)
        inputNotes.send_keys(notesText)

        # For now she types in enter in the notes box to send the information
        # Later, there will be a submit button once we get to forms

        submitButton.click()
        time.sleep(1)

        #The first case now appears in the table
        # Test to make sure info was submitted 
        table = self.browser.find_element_by_id('id_table')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn(dateText, [row.text for row in rows])
        self.assertIn(timeText, [row.text for row in rows])
        self.assertIn(locationText, [row.text for row in rows])
        self.assertIn(youthNameText, [row.text for row in rows])
        self.assertIn(notesText, [row.text for row in rows])
    
        self.fail('Finish the test')

#Done for now

if __name__ == '__main__':
    unittest.main() #warnings='ignore')



