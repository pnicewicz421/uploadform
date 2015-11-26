from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {
        'date_text': request.POST.get('date_text', ''),
        'time_text': request.POST.get('time_text', ''),
        'location_text': request.POST.get('location_text', ''),
        'youth_name_text': request.POST.get('youth_name_text', ''),
        'notes_text': request.POST.get('notes_text', '')
    })