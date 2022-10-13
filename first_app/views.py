from multiprocessing import context
from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord
from django.http import HttpResponse

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {'insert_me':"Hello am from the views.py !"}

    return render(request,'first_app/index.html',context=date_dict)

def help(request):
    helpdict = { 'help_insert':"HELP PAGE"}


    return render(request,'first_app/help.html',context=helpdict)

def about(request):
    aboutdict = { 'about_insert':"ABOUT PAGE"}

    return render(request,'first_app/about.html',context=aboutdict)
    