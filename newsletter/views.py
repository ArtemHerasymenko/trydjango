from django.shortcuts import render
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
	


	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():
		print("Form body = ", str(form.cleaned_data))

	context = {
		"form" : form
	}

	return render(request, "form.html", context)