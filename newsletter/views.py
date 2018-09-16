from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, ContactForm

# Create your views here.

def home(request):
	title = "My title"
	name = "Welcome"

	if(request.user.is_authenticated()):
		name = request.user

	form = SignUpForm(request.POST or None)
	
	context = {
		"title" : title,
		"name" : name,
		"form" : form
	}

	if form.is_valid():
		print("Form Is Valid")
		instance = form.save()
		print("Instance = ",instance)
		print(instance.email)
		print(instance.timestamp)
		context = {
			"title" : "Thank you"
		}
	

	print("method=",request.method)
	print("POST=",request.POST)
	print("GET=",request.GET)
	


	return render(request, "base.html", context)

def contact(request):
	form = ContactForm(request.POST or None)

	my_email = settings.EMAIL_HOST_USER

	if form.is_valid():
		email_to_send = form.cleaned_data.get('email')
		print("Sending email to %s" %(email_to_send))
		send_mail(
			'My Subject',
			'MEssgae from trydjango',
			my_email,
			[my_email],
			fail_silently=False,
			)

	context = {
		"form" : form
	}

	return render(request, "form.html", context)