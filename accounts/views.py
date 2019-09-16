from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from utils import provinces
from .models import User
from .forms import PreferencesForm

@login_required(login_url="account_login")
def settings(request):
	provs = provinces.get_provinces()
	preferences_form = PreferencesForm(initial={'bill_contact': request.user.bill_contact, 'promo_contact': request.user.promo_contact})
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		if request.POST['first_name']:
			user.first_name = str(request.POST['first_name'])
		if request.POST['last_name']:
			user.last_name = str(request.POST['last_name'])
		if request.POST['city']:
			user.city = str(request.POST['city'])
		if request.POST['province']:
			user.province = request.POST['province']
		if request.POST['age']:
			user.age = request.POST['age']
		if request.POST['gender']:
			user.gender = request.POST['gender']
		if request.POST['phone_number']:
			prev_phone_number = user.phone_number
			new_phone_number = request.POST['phone_number']
			if new_phone_number != prev_phone_number:
				user.phone_number_verified = False
				user.phone_number = new_phone_number
		user.save()
		messages.success(request, 'Your settings have been saved!.')
		return redirect('settings')
	else:
		return render(request, 'account/settings.html', {'provinces': provs, 'preferences_form':preferences_form})

@login_required(login_url="account_login")
def preferences(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		preferences_form = PreferencesForm(request.POST)
		if preferences_form.is_valid():
			user.bill_contact = preferences_form.cleaned_data['bill_contact']
			user.promo_contact = preferences_form.cleaned_data['promo_contact']
			user.save()
			messages.success(request, 'Your preferences have been saved!.')
	return redirect('settings')