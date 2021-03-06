"""records URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib import views

from rhymis import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),  #Index
    url(r'^records/new$', views.newrecord, name='newrecord'), #New Record
    url(r'^records/new/process$', views.processrecord, name='processrecord'), #Process a New Record
    url(r'^records/edit/process$', views.processedit, name='processedit'), #Process and Edited Record
    url(r'^records/view$', views.viewrecords, name='viewrecords'), #View All Records 
    url(r'^records/view/(?P<field>youth|location|staff)/(?P<keyword>\w+)$', views.viewrecords, name='viewrecords'), #View Some Records by Field and Keyword
    url(r'^records/view/(?P<field>date)/(?P<keyword>\d+\/\d+\/\d+)$', views.viewrecords, name='viewrecords'), #View Records By Date
    url(r'^records/delete/(\d+)$', views.deleterecord, name='deleterecord'), #Delete Record 
    url(r'^records/upload$', views.upload_file, name='uploadfile'), #Upload File
    url(r'^records/handlefile$', views.handle_file, name='handlefile'), #Handle a particular uploaded file
    url(r'^records/forms.html$', views.upload_file, name='uploadfile'), #Upload File
    url(r'^records/signup/$', views.sign_up, name='signup'),
    url(r'^login/$', views.user_login, name='account_login'), #CAREFUL - Django Auth View
    url(r'^logout/$', views.user_logout, name='account_logout'), #AGAIN, careful
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]
