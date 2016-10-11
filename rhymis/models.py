from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    locationName = models.TextField(max_length='45', default='')
    
class Record(models.Model):    
    datetimeText = models.TextField(max_length='30')
    staffText = models.TextField(default='')
    locationText = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    youthNameText = models.TextField(default='')
    notesText = models.TextField(default='')
    
class FileUpload(models.Model):
    filename = models.FileField(upload_to = 'files/') #don't need upload_to if MEDIA_ROOT is defined in settings.py
    
class ZIPStructure(models.Model): #This model tracks the directories and files that are extracted
    ZIPDirectory = models.TextField
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    
    #list of locations for user?
    locations = models.ManyToManyField(Location)
    
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
        
    class Meta:
        db_table = 'user_profile'
        
    #def account_verified(self):
     #   if self.user.is_authenticated:
      #      result = EmailAddress.objects.filter(email=self.user.email)
       #     if len(result):
        #        return result[0].verified
        #return False
        
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    