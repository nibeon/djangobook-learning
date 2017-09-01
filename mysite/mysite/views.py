#from django.http import HttpResponse
#from django.template.loader import get_template
#import datetime
#

from django.shortcuts import render
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

#def hello(request):
#	return HttpResponse("Hello World")
	
#def current_datetime(request):
#	now = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render({'current_date': now})
#	return HttpResponse(html)
