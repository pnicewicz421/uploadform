from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from rhymis.forms import UploadFileForm, UserForm, UserProfileForm
from rhymis.models import Record, Location, FileUpload, ZIPStructure, UserProfile
from urllib.parse import urlparse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import rhymis.libraries.logic as lg

#from somewhere import handle_uploaded_file 
    #-- we will develop this function to process the file


# Create your views here.

#Index: display all of your records
def index_view(request):
    context = RequestContext(request)
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations}, context)
    
def newrecord(request):
    #Add a new record
    return render(request, 'newrecord.html')

@login_required 
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

def processedit(request):
    #process the edit
    if request.method == 'POST':
        recordid = request.POST['-1']
        record = Record.objects.get(pk=recordid)
        record.datetimeText = request.POST.get('0','')
        record.locationText.locationName = request.POST.get('1','')
        record.staffText = request.POST.get('2')
        record.youthNameText = request.POST.get('3','')  
        record.notesText = request.POST.get('4')
        record.save()

        #take the results from the saved database and save them in response_data
        response_data = {}
        response_data[-1] = recordid
        response_data[0] = record.datetimeText
        response_data[1] = record.locationText.locationName
        response_data[2] = record.staffText
        response_data[3] = record.youthNameText
        response_data[4] = record.notesText
        
        return JsonResponse(response_data)

        #HttpResponse(
         #   json.dumps(response_data),
          #  content_type = "application/json"
        #)

    else:
        return JsonResponse({'result':'error', 'error': 'get_request'})

        #HttpResponse(
         #   json.dumps({"error": "get_request"}),
          #  content_type = "application/json"
        #)


@login_required    
def viewrecords(request, field=None, keyword=None): #optionally pass the field (either 'date' or 'location' or 'youth') and keyword to be filtered
    #if not request 
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

@login_required
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
            filename = FileUpload(filename = request.FILES['filename'])
            filename.save()
            # html = '<html><body>The form was valid. Form was %s. Filename was %s (model). finally, in the post request. Request.FILES[\'filename\'] was %s </body></html>' % (form, filename, request.FILES['filename'])
            return redirect('/records/handlefile')
    else:
        form = UploadFileForm() #empty, unbound form
        files = FileUpload.objects.all()
        return render(request, 'uploadform.html', {'documents': files, 'form': form})
        
def handle_file(request):
    length = len(FileUpload.objects.all())
    filename = FileUpload.objects.all()[length - 1]
    
    # first check to see if it's a zip file
    response = lg.CheckifZipFile(filename)
    filedir = lg.CheckifRightMembers(filename)
    
    #Extract each member (note: not all files necessarily) and save each file on the disk (not read into memory)
    #mmm = lg.ExtractMembers(ZIPfile)
    
    #Go through the Files that have Fields with Hash requirements
    
    #processhash = lg.CheckifHashed(filename)
    
    #Attempt to Hash it for them.
    
    
    html = "<html><body> Extracted the following files: %s </body></html>" % revlist
    return HttpResponse(html)

#Registration (Sign-up) view
#we need a template to sign people up
def sign_up(request):
        
    signedup = False #Whether the user has signed up successfully
    
    if request.method == 'POST':
        #grab the info from the two forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password) #hash the password
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()
            
            signedup = True
        else:
            print (user_form.errors, profile_form.errors)
            
    else:
        #GET request
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form, 'signedup': signedup})

#Login view 
#we need a template to 
def user_login(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #attempt to log in. If the User is not authenicated (username and password don't match), 
        #then return False  
        user = authenticate(username=username, password=password)
        
        if user:
            #check if active
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/records/view')
                #redirect('/records/view') 
            else:
                return HttpResponse("<html><body><h1>Account Disabled</h1><br>Your account has been disasbled (User not active). Contact your administrator for assistance.</body></html>")
        else:
            #invalid logon details
            return HttpResponse("Invalid login details.")
    else:
        #not a POST request
        return render(request, 'logins.html', {}, context)
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile_view(request):
    #allauth.account.signals.user_logged_in(request, user)
   # a = request.user.first_name
    #b = request.user.last_name
    #c = request.user.username
    #d = request.user.is_authenticated
    #html = "<html><body>%s</body></html>" % c
    return render_to_response("index.html", RequestContext(request))

# P1etralikownaya1209$$

# Client ID 847944008317-onn0h8qql3vej40kod5tjmukpdccb29a.apps.googleusercontent.com 
#Client Secret:  mVlKOD5-mGMSCYNtncAmPZbr 