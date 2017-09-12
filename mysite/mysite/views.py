from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm    
from django.core.mail import send_mail, get_connection

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now        
    return HttpResponse(html)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
				connection=con
			)
			return HttpResponseRedirect('/contact/thanks')
		else:
			form = ContactForm()

		return render(request, 'contact_form.html', {'form': form})