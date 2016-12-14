from django.http import HttpResponse  
import datetime
from django.shortcuts import render
	
def current_datetime(request):
	now=datetime.datetime.now()
	html = "it is now %s."%now 
	return HttpResponse(html)
	
def hours_ahead(request,offset):
	try:
		offset = int(offset)
		pass
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	html = "in %s hours,it will be %s"%(offset,dt)
	return HttpResponse(html)

"""
The point of this example was to demonstrate Django’s error pages. Take some time to explore the error page and get to know the various bits of information it gives you. Here are some things to notice

At the top of the page, you get the key information about the exception: the type of exception, any parameters to the exception (the "unsupported type" message in this case), the file in which the exception was raised, and the offending line number.

Under the key exception information, the page displays the full Python traceback for this exception. This is similar to the standard traceback you get in Python’s command-line interpreter, except it’s more interactive. For each level (“frame”) in the stack, Django displays the name of the file, the function/method name, the line number, and the source code of that line.

Click the line of source code (in dark gray), and you’ll see several lines from before and after the erroneous line, to give you context. Click “Local vars” under any frame in the stack to view a table of all local variables and their values, in that frame, at the exact point in the code at which the exception was raised. This debugging information can be a great help.

Note the “Switch to copy-and-paste view” text under the “Traceback” header. Click those words, and the traceback will switch to an alternate version that can be easily copied and pasted. Use this when you want to share your exception traceback with others to get technical support – such as the kind folks in the Django IRC chat room or on the Django users mailing list.

Underneath, the “Share this traceback on a public Web site” button will do this work for you in just one click. Click it to post the traceback to dpaste, where you’ll get a distinct URL that you can share with other people.

Next, the “Request information” section includes a wealth of information about the incoming Web request that spawned the error: GET and POST information, cookie values, and meta information, such as CGI headers. Appendix F has a complete reference of all the information a request object contains.

Below the “Request information” section, the “Settings” section lists all of the settings for this particular Django installation. All the available settings are covered in detail in Appendix D.
"""