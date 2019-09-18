import random

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
	return render(request, 'main/home.html')

def about(request):
	return render(request, 'main/about.html')

def contactus(request):
	return render(request, 'main/contactus.html')

def licenses(request):
	return render(request, 'main/licenses.html')

def privacypolicy(request):
	return render(request, 'main/privacypolicy.html')

def termsofuse(request):
	return render(request, 'main/termsofuse.html')

def permission_denied(request, exception):
	print(exception.message)
	return render(request, 'main/403.html')

def page_not_found(request, exception):
	return render(request, 'main/404.html')

def server_error(request):
	return render(request, 'main/500.html')

@staff_member_required
def sandbox(request):
	return render(request, 'main/sandbox.html')