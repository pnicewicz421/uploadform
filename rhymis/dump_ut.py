#class index_viewTest(TestCase):
 #   
  #  def test_uses_view_template_after_GET_request(self):
   #     record_number = RecordNumber.objects.create()
    #    response = self.client.get('/records/%d/' % (record_number.id,))
    #    self.assertTemplateUsed(response, 'viewrecord.html')
   # 
   # def test_root_url_resolves_to_index_view(self):
   #     found = resolve('/')
   #     self.assertEqual(found.func, index_view)
   #     
   # def test_index_view_returns_correct_html(self):
   #     request = HttpRequest()
   #     response = index_view(request)
   #     expected_html = render_to_string('index.html')
   #     
    #    print (expected_html)
     #   print ()
       #print (response.content.decode())
       
        #self.assertEqual(response.content.decode(), expected_html)
        
   # def test_index_view_does_not_save_blank_entries(self):
    #    request = HttpRequest()
     #   index_view(request)
      #  self.assertEqual(Record.objects.count(), 0)
        
#!
#class change_recordsTest(TestCase):
    ###
 #   def test_multiple_lists(self):
  #      gmt5 = GMT5()
   #     record_number1 = RecordNumber()
    #    record_number1.save()
     #   
      #  record_number2 = RecordNumber()
     #  # record_number2.save()
    
       # locationText1 = 'Home'
      #  locationText2 = 'Washington'
        
        #Record.objects.create(datetimeText=datetime.datetime(2015, 1, 23, 4, 56, tzinfo=gmt5), locationText=locationText1, youthNameText='Monty Python', notesText='The notes are here', recordNumberText=record_number1)
        #Record.objects.create(datetimeText=datetime.datetime(2016, 11, 15, 23, 1, tzinfo=gmt5), locationText=locationText2, youthNameText='White House', notesText='Bad News', recordNumberText=record_number2)
    
        #response = self.client.post('/records/%d/' % (record_number1.id,), {'date_time_text': datetime.datetime(2015, 1, 23, 4, 56, tzinfo=gmt5), 'location_text':locationText1, 'youth_name_text':'Monty Python', 'notes_text'='The notes are here', 'record_number_text'=record_number1})
        
        #print ('The response',)
        #print (response.content.decode())
        
        #self.assertContains(response, locationText1)
        #self.assertNotContains(response, locationText2)
        
       # response = self.client.get('/records/%d/' % (record_number2.id,))
        
        #print (response)
        
        #self.assertContains(response, locationText2)
        #self.assertNotContains(response, locationText1)
        
#view a particular set of records (RecordNumber)
class NewRecordNumberTest(TestCase):
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
        
        gmt5 = GMT5()
        datetimeText = datetime.datetime(2015, 11, 21, 14, 37, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        print("ABOUT to POST")
        
        self.client.post('/records/new', data=
            {'date_time_text': datetimeText, 'location_text': locationText, 
            'youth_name_text': youthNameText, 'notes_text': notesText})
    
        self.assertEqual(Record.objects.count(), 1)
        new_record = Record.objects.first()
        self.assertEqual(new_record.datetimeText, datetimeText)
        self.assertEqual(new_record.locationText, locationText)
        self.assertEqual(new_record.youthNameText, youthNameText)
        self.assertEqual(new_record.notesText, notesText)

    
    def test_index_view_redirects_after_POST_request(self):        
        gmt5 = GMT5()
        datetimeText = datetime.datetime(2015, 11, 21, 14, 37, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        response = self.client.post('/records/new', data=
            {'date_time_text': datetimeText, 'location_text': locationText, 
            'youth_name_text': youthNameText, 'notes_text': notesText})
            
        record_number = RecordNumber.objects.first()
        self.assertRedirects(response, '/records/%d/' % (record_number.id,))
        
    def test_redirects_to_an_existing_record_number(self):
        gmt5 = GMT5()
        datetimeText = datetime.datetime(2015, 11, 21, 14, 37, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        record_number1 = RecordNumber.objects.create()
        record_number2 = RecordNumber.objects.create()
        
        print ("BOOOO: %d" % (record_number2.id,))
        
        response = self.client.post(
            '/records/%d/add_record' % (record_number2.id,), data=
            {'date_time_text': datetimeText, 'location_text': locationText, 
            'youth_name_text': youthNameText, 'notes_text': notesText})
            
        self.assertRedirects(response, '/records/%d/' % (record_number2.id,))
        
    def test_saving_an_additional_record_to_an_existing_record_number(self):
        gmt5 = GMT5()
        datetimeText = datetime.datetime(2015, 11, 21, 14, 37, tzinfo=gmt5)
        locationText = 'Woodberry Park'
        youthNameText = 'Grazyna Kwiatkowska'
        notesText = 'Testing notes'
        
        record_number1 = RecordNumber.objects.create()
        record_number2 = RecordNumber.objects.create()
        
        response = self.client.post(
            '/records/%d/add_record' % (record_number2.id,), data=
            {'date_time_text': datetimeText, 'location_text': locationText, 
            'youth_name_text': youthNameText, 'notes_text': notesText})
            
        self.assertEqual(Record.objects.count(), 1)
        the_record = Record.objects.first()
        self.assertEqual(the_record.locationText, locationText)
        self.assertEqual(the_record.recordNumberText, record_number2)

class GMT5(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=5)
        
    def dst(self, dt):
        return datetime.timedelta(0)
    
class RecordandRecordNumberModelTest(TestCase):
    
    def test_save_and_retrieve(self):
        gmt5 = GMT5()
        
        record_number=RecordNumber()
        record_number.save()
        
        first_record = Record()
        first_record.datetimeText = datetime.datetime(2015, 11, 26, 15, 32, tzinfo=gmt5)
        #first_record.timeText = datetime.time(15, 32) #EST
        first_record.locationText = 'OT'
        first_record.youthNameText = 'Oscar Peterson'
        first_record.notesText = 'OP was the OG even before the term was coined'
        first_record.recordNumberText = record_number
        first_record.save()
        
        second_record = Record()
        second_record.datetimeText = datetime.datetime(1967, 1, 25, 3, 41, tzinfo=gmt5)
        #second_record.timeText = datetime.time(3, 41) #UTC
        second_record.locationText = 'Reykjavik'
        second_record.youthNameText = 'Olaf the Hippie'
        second_record.notesText = 'Made up viking hippie. Is that a thing'
        second_record.recordNumberText = record_number
        second_record.save()
        
        saved_records = RecordNumber.objects.first()
        self.assertEqual(saved_records, record_number)
        
        saved_items = Record.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.datetimeText, datetime.datetime(2015, 11, 26,15, 32, tzinfo=gmt5))
        self.assertEqual(first_saved_item.locationText, 'OT')
        self.assertEqual(first_saved_item.youthNameText, 'Oscar Peterson')
        self.assertEqual(first_saved_item.notesText, 'OP was the OG even before the term was coined')
        self.assertEqual(first_saved_item.recordNumberText, record_number)
        
        self.assertEqual(second_saved_item.datetimeText, datetime.datetime(1967, 1, 25, 3, 41, tzinfo=gmt5))
        self.assertEqual(second_saved_item.locationText, 'Reykjavik')
        self.assertEqual(second_saved_item.youthNameText, 'Olaf the Hippie')
        self.assertEqual(second_saved_item.notesText, 'Made up viking hippie. Is that a thing')
        self.assertEqual(second_saved_item.recordNumberText, record_number)
        
    #def test_passes_correct_records_to_RecordNumber(self):
     #   other_RecordNumber = RecordNumber.objects.create()
      #  correct_RecordNumber = RecordNumber.objects.create()
       # response = self.client.get('/records/%d' % (correct_RecordNumber.id,))
        # print ("HERERERAERAERREERE"),
      #  print (response.context['record'])
        #self.assertEqual(response.context['record_number'], correct_RecordNumber)
        