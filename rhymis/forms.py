from django import forms
from rhymis.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('locations',)

class UploadFileForm(forms.Form):
    filename = forms.FileField(
        label='Select a file',
        help_text='select up to 42 mgbs',
    )