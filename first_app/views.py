from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello am from the views.py !"}

    return render(request,'first_app/index.html',context=my_dict)

def help(request):
    helpdict = { 'help_insert':"HELP PAGE"}


    return render(request,'first_app/help.html',context=helpdict)

def about(request):
    aboutdict = { 'about_insert':"ABOUT PAGE"}

    return render(request,'first_app/about.html',context=aboutdict)
    