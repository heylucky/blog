from django.http import HttpResponse  
import datetime
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world,lin yue lin")
	
def linyuelin(request):
	return HttpResponse("CONGRADUALATION!!!")

def my_homepage_view(request):
	return render(request,'blog/templates/temp_blog/ai5.html',{})
	
def current_datetime(request):
	now=datetime.datetime.now()
	html = "it is now %s."%now 
	return HttpResponse(html)