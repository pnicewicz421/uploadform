from django.db import models
from datetime import datetime

class Record(models.Model):
    
    CENTERS = (
    ('WP', 'Woodberry Park'),
    ('GB', 'Gates of Ballston'),
    ('FH', 'Fort Henry'),
    ('OT', 'Other'),
    )
    
    datetimeText = models.DateTimeField('date and time case opened', default=None, null=True, blank=True)
    locationText = models.CharField(max_length='30', choices=CENTERS, default='OT')
    youthNameText = models.TextField(default='')
    notesText = models.TextField(default='')