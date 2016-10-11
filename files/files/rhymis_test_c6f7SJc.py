from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Open webpage

        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # "To-Do" in title and header

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Make sure that inputbox 'placeholder' attribute is equal to "Enter a to-do item
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # Enter "buy peacock feathers" to the input field and send

        self.get_item_input_box().send_keys('Buy peacock feathers')
        self.get_item_input_box().send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url

        # print ("Edith's URL: %s" % edith_list_url)

        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        self.get_item_input_box().send_keys('Use peacock feathers to make a fly'
                )
        self.get_item_input_box().send_keys(Keys.ENTER)

        # After a refresh, make sure that that input now appears in the row in the table

        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly'
                )
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Now a new user comes to the site

        # #new, browser, so that cookies are not stored

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. No sign of Edith's list.

        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis' list

        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Francis gets his own URL

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, 'lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # No trace of Edith's list

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feather', page_text)
        self.assertIn('Buy milk', page_text)
		
		
