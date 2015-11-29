from django.shortcuts import render, redirect
from django.http import HttpResponse
from rhymis.models import Record, RecordNumber

# Create your views here.

#Index: display all of your records
def index_view(request):
    
    record = Record()
    record.datetimeText = request.POST.get('date_time_text', None)
    record.locationText = request.POST.get('location_text', '')
    record.youthNameText = request.POST.get('youth_name_text', '')
    record.notesText = request.POST.get('notes_text', '')
    
    record_number = RecordNumber.objects.create()
    record.recordNumberText = record_number
        
    if request.method == 'POST':
        record.save()
        return redirect('/records/list-identifier/')

    records = Record.objects.all()
    return render(request, 'index.html', {'records': records})
    
#Change record action - to redirect after POST    
def change_records(request):
    records = Record.objects.all()
    return render(request, 'index.html', {'records': records})