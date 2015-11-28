from django.shortcuts import render, redirect
from django.http import HttpResponse
from rhymis.models import Record

# Create your views here.
def index_view(request):
    
    record = Record()
    record.datetimeText = request.POST.get('date_time_text', None)
    record.locationText = request.POST.get('location_text', '')
    record.youthNameText = request.POST.get('youth_name_text', '')
    record.notesText = request.POST.get('notes_text', '')
        
    if request.method == 'POST':
        record.save()
        return redirect('/')

    records = Record.objects.all()
    return render(request, 'index.html', {'records': records})
        #'date_time_text': (record.datetimeText if record.datetimeText is not None else ''),
       # 'location_text': record.locationText,
      #  'youth_name_text': record.youthNameText,
     #   'notes_text': record.notesText
    #})       