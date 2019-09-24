from urllib.request import urlopen

import requests
from django.contrib import messages
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from houses.models import House
from utils.captcha import Captcha
from utils.emailclient import send_contact_us_email
from utils.ipaddress import get_IP
from .models import ContactMessage
from django.conf import settings

from utils.models import PrivateImage


def home(request):
	return render(request, 'main/home.html')


def about(request):
	return render(request, 'main/about.html')


def contactus(request):
	captcha = Captcha()
	if request.method == 'POST':
		ip = get_IP(request)
		send_contact_us_email(request.POST['sender_email'], request.POST['subject'], request.POST['message'], ip)
		message = ContactMessage()
		message.sender = request.POST['sender_email']
		message.subject = request.POST['subject']
		message.message = request.POST['message']
		message.ip = ip
		message.save()

		messages.success(request, 'We have received your contact request and will get back to you as soon as possible!.')
		return redirect('home')
	return render(request, 'main/contactus.html', {'captcha': captcha})


# TODO Finish
def reportbug(request):
	return render(request, 'main/reportbug.html')


def licenses(request):
	return render(request, 'main/licenses.html')


def privacypolicy(request):
	return render(request, 'main/privacypolicy.html')


def termsofuse(request):
	return render(request, 'main/termsofuse.html')


def permission_denied(request, exception):
	return render(request, 'main/403.html')


def page_not_found(request, exception):
	return render(request, 'main/404.html')


def server_error(request):
	return render(request, 'main/500.html')


@staff_member_required
def sandbox(request):
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	url = 'https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&key={}'.format(GOOGLE_API_KEY)
