from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    myresponse = '<html><title>Issue Tracker</title></html>'
    return HttpResponse(myresponse)