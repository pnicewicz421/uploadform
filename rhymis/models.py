from django.db import models
from datetime import datetime

class Location(models.Model):
    locationName = models.TextField(max_length='45', default='')
    
class Record(models.Model):    
    datetimeText = models.TextField(max_length='30')
    staffText = models.TextField(default='')
    locationText = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    youthNameText = models.TextField(default='')
    notesText = models.TextField(default='')
    
class Document(models.Model):
    filename = models.FileField(upload_to = 'files/') #don't need upload_to if MEDIA_ROOT is defined in settings.py