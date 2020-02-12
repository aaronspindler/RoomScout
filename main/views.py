from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.conf import settings

from bills.forms import BillFormset
from utils.captcha import Captcha
from emails.senders import send_contact_us_email
from security.helpers import get_IP
from .models import ContactMessage


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

		messages.success(request, 'We have received your contact request and will get back to you as soon as possible!')
		return redirect('home')
	return render(request, 'main/contactus.html', {'captcha': captcha})


def billfeatures(request):
	return render(request, 'main/billfeatures.html')


def supportus(request):
	key = settings.STRIPE_KEY
	return render(request, 'main/supportus.html', {'key': key})


def verificationfeatures(request):
	return render(request, 'main/verificationfeatures.html')


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


@staff_member_required(login_url="account_login")
def sandbox(request):
	if request.method == 'POST':
		print(request.POST)
		formset = BillFormset(request.POST)
		if formset.is_valid():
			for form in formset:
				print(form.cleaned_data)
		else:
			print('invalid')
	formset = BillFormset()
	return render(request, 'main/sandbox.html', {'formset': formset})
