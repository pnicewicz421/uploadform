from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_right_title(self):
        #Of course, let's make sure that Issue Tracker apperas in the title.
        self.browser.get('http://localhost:8000')
        self.assertIn('Issue Tracker', self.browser.title)
        self.fail('Finish the test!')
        
#She sees a table with headers labeled: 
#   - Date (date field)
#   - Time (date field)
#   - Location (text field; 50 chars max)
#   - Youth Name (text field; 50 chars max)
#   - Notes (text field; 500 chars max)

#She also sees blank fields below the header ready to populate the table

#She sees a submit button

#She types in her first case:
#   - Date: 11/21/2015
#   - Time: 2:37 PM EST
#   - Location: Woodberry Park
#   - Youth Name: Grazyna Kwiatkowska
#   - Notes: Grazyna came crying after her cajun-style grilled cheese sandwich
#   - with red peppers and stuffed portabello mushrooms turned out 
#   - slightly burnt. New grilled cheese was issued. Issue resolved. 

#She clicks the submit button

#The first case now appears in the table

#Done for now

if __name__ == '__main__':
    unittest.main() #warnings='ignore')



