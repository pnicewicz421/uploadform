  table = self.browser.find_element_by_id('id_table')
        headers = table.find_elements_by_tag_name('th')
        
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
        
        dateTimeText = datetime.datetime(2015, 11, 21, 15, 21, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        row_text = [str(dateTimeText), locationText, youthNameText, notesText]
        
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
        
        #Test second item -- see need for refactor?
        inputDateTime = self.browser.find_element_by_id('id_date_time')
        inputLocation = self.browser.find_element_by_id('id_location')
        inputYouthName = self.browser.find_element_by_id('id_youth_name')
        inputNotes = self.browser.find_element_by_id('id_notes')
        
        submitButton = self.browser.find_element_by_id('id_submit')
        dateTimeText = datetime.datetime(2020, 12, 31, 23, 1, tzinfo=gmt5)
        locationText = 'The Beach'
        youthNameText = 'No Homeless Youth'
        notesText = 'Happy New Year'
        inputDateTime.send_keys(str(dateTimeText))
        inputLocation.send_keys(locationText)
        inputYouthName.send_keys(youthNameText)
        inputNotes.send_keys(notesText)
        submitButton.click()
        
        time.sleep(10)
        
        row_text1 = [str(dateTimeText), locationText, youthNameText, notesText]
        self.check_for_row_in_table(row_text)
        self.check_for_row_in_table(row_text1)
        
        #Second user comes along
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        self.browser.get(self.live_server_url)
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