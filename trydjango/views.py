from django.shortcuts import render
from newsletter.models import SignUp

def about(request):

	content = {
		
	}

	if request.user.is_authenticated() and request.user.is_staff:
		content = {
			"queryset" : SignUp.objects.all().order_by("-timestamp")
		}

	return render(request, "about.html", content)