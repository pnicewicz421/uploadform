from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UploadFileForm
from rhymis.models import Record, Location, Document

from urllib.parse import urlparse

#from somewhere import handle_uploaded_file 
    #-- we will develop this function to process the file


# Create your views here.

#Index: display all of your records
def index_view(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations})
    
def newrecord(request):
    #Add a new record
    return render(request, 'newrecord.html')

def processrecord(request):
    location = request.POST['location_text'].strip()
    storedlocation = Location.objects.filter(locationName=location)
    if storedlocation.count() == 0:
        #New location. Create a new Location field.
        newlocation = Location.objects.create(locationName=location)
    else:
        #Location used before. Store there.
        newlocation = Location.objects.get(locationName=location)
    Record.objects.create(datetimeText=request.POST['date_time_text'], locationText=newlocation, staffText=request.POST['staff_text'], youthNameText=request.POST['youth_name_text'].strip(), notesText=request.POST['notes_text'].strip())
    
    referurl = urlparse(request.META['HTTP_REFERER'])
    referpath = referurl.path
    if referpath=='/records/view/location/%s' % location:
        return redirect('/records/view/location/%s' % location) #Result will be viewing the records at that location
    return redirect('/records/view') 
    
def viewrecords(request, field=None, keyword=None): #optionally pass the field (either 'date' or 'location' or 'youth') and keyword to be filtered
    if field is None and keyword is None:
        #View all records
        records = Record.objects.all() 
        message = 'View All Records'
    elif field == 'youth':
        message = 'View Records for %s' % keyword
        records = Record.objects.filter(youthNameText=keyword)
    elif field == 'location':
        message = 'View Records at %s' % keyword
        location = Location.objects.get(locationName=keyword)
        records = Record.objects.filter(locationText=location)
    elif field == 'staff':
        message = 'View Record for Staff: %s' % keyword
        records = Record.objects.filter(staffText=keyword)
    elif field == 'date':
        message = 'View Records on Date: %s' % keyword
        records = Record.objects.filter(datetimeText=keyword)
    return render(request, 'viewrecord.html', {'message': message, 'records': records})

def deleterecord(request, recordid):
    #If only record, delete the location, otherwise delete the unwanted record, redirect to referring path
    referurl = urlparse(request.META['HTTP_REFERER'])
    referpath = referurl.path
    record = Record.objects.get(id=recordid)
    location = record.locationText   
    recordsleft = Record.objects.filter(locationText=location)
    if recordsleft.count() == 1:
        location.delete()
        return redirect('/')
    record.delete()
    return redirect(referpath)
    
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES) #form
        if form.is_valid():
            #save the file into the database 
            filename = Document(filename = request.FILES['filename'])
            filename.save()
            html = '<html><body>The form was not valid. Form was %s. Filename was %s (model). finally, in the post request. Request.FILES[\'filename\'] was %s </body></html>' % (form, filename, request.FILES['filename'])
            return HttpResponse(html)
        else:
            form = UploadFileForm() #empty, unbound form
            
        files = Document.objects.all()
                
        html = '<html><body>The form was not valid. Form was %s. Files: %s</body></html>' % (form, files)
        return HttpResponse(html)
    else:
        html = '<html><body>GET request</body></html>'
        return HttpResponse(html)
    