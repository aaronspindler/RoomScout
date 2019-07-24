from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from utils import provinces, emailclient
from .models import User


def login(request):
	if request.POST:
		print(request.META.get('REMOTE_ADDR'))
		username = request.POST['username']
		password = request.POST['password']
		if username == '' or password == '':
			return render(request, 'registration/login.html', {'error': 'Username or Password cannot be blank!'})
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'registration/login.html', {'error': 'Username or Password is incorrect!'})
	return render(request, 'registration/login.html')


def signup(request):
	# Check if its a post request
	# Check if passwords match
	# Check if username, password, or email are blank
	# Check if user with same username exists
	# Check if user with same email exists
	# Check for first or last name
	# Check if first or last name are blank
	provs = provinces.get_provinces()
	if request.method == 'POST':
		if request.POST['username'] == '' or request.POST['password1'] == '' or request.POST['password2'] == '' or \
				request.POST['email'] == '':
			return render(request, 'accounts/signup.html',
			              {'error': 'Username/Password/Email cannot be blank!', 'provinces': provs})
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html',
				              {'error': 'Username has already been taken!', 'provinces': provs})
			except User.DoesNotExist:
				try:
					user = User.objects.get(email=request.POST['email'])
					return render(request, 'accounts/signup.html',
					              {'error': 'Email is already in use!', 'provinces': provs})
				except User.DoesNotExist:
					if request.POST['first_name'] and request.POST['last_name']:
						if request.POST['first_name'] == '' or request.POST['last_name'] == '':
							return render(request, 'accounts/signup.html',
							              {'error': 'First/Last name cannot be blank!', 'provinces': provs})
						email = request.POST['email']
						username = request.POST['username']
						password = request.POST['password1']
						firstname = request.POST['first_name']
						lastname = str(request.POST['last_name'])
						if request.POST['address']:
							address = str(request.POST['address'])
						else:
							address = None

						if request.POST['province']:
							prov_state = request.POST['province']
						else:
							prov_state = None

						if request.POST['city']:
							city = str(request.POST['city'])
						else:
							city = None

						if request.POST['postal_code']:
							postal_code = str(request.POST['postal_code'])
						else:
							postal_code = None

						user = User.objects.create_user(username, password=password)
						user.ip_address = request.META.get('REMOTE_ADDR')
						user.email = email
						user.previous_email = email
						user.first_name = firstname
						user.last_name = lastname
						user.address = address
						user.city = city
						user.prov_state = prov_state
						user.postal_code = postal_code
						user.score = 0.0
						user.save()
						emailclient.send_confirmation_email()
						auth.login(request, user)
						return redirect('home')
					else:
						return render(request, 'accounts/signup.html',
						              {'error': 'Please enter your first and last name!', 'provinces': provs})

		else:
			return render(request, 'accounts/signup.html', {'error': 'Passwords must match!', 'provinces': provs})
	else:
		return render(request, 'accounts/signup.html', {'provinces': provs})


@login_required(login_url="/login")
def settings(request):
	provs = provinces.get_provinces()
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		if request.POST['email']:
			if request.POST['email'] == '':
				pass
			else:
				if request.POST['email'] != user.email:
					try:
						user = User.objects.get(email=request.POST['email'])
						return render(request, 'accounts/settings.html',
						              {'error': 'Email is already in use!', 'provinces': provs})
					except User.DoesNotExist:
						if user.email_confirmed:
							user.previous_email = user.email
					user.email_confirmed = False
					emailclient.send_confirmation_email()
					user.email = request.POST['email']
		if request.POST['address']:
			user.address = str(request.POST['address'])
		if request.POST['city']:
			user.city = str(request.POST['city'])
		if request.POST['province']:
			user.province = request.POST['province']
		if request.POST['postal_code']:
			user.postal_code = str(request.POST['postal_code'])
		user.save()
		messages.success(request, 'Your settings have been saved!.')
		return redirect('home')
	else:
		return render(request, 'accounts/settings.html', {'provinces': provs})
