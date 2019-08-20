from django.shortcuts import render


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
