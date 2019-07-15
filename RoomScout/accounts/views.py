from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django_countries import countries

from .models import User
from utils import provinces, email

def signup(request):
    provs = provinces.get_provinces()
    if request.method == 'POST':
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken!', 'provinces':provs})
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email = request.POST['email'])
                    return render(request, 'accounts/signup.html', {'error':'Email is already in use!', 'provinces':provs})
                except User.DoesNotExist:
                    if request.POST['firstname'] and request.POST['lastname']:
                        email = request.POST['email']
                        username = request.POST['username']
                        password = request.POST['password1']
                        firstname = request.POST['firstname']
                        lastname = str(request.POST['lastname'])
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
                        user.email = email
                        user.first_name = firstname
                        user.last_name = lastname
                        user.address = address
                        user.city = city
                        user.prov_state = prov_state
                        user.postal_code = postal_code
                        user.score = 0.0
                        user.save()
                        email.send_confirmation_email()
                        login(request,user)
                        return redirect('home')
                    else:
                        return render(request, 'accounts/signup.html', {'error':'Please enter your first and last name!', 'provinces':provs})

        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match!', 'provinces':provs})
    else:
        return render(request, 'accounts/signup.html', {'provinces':provs})

def settings(request):
    provs = provinces.get_provinces()
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        if request.POST['email']:
            if request.POST['email'] != user.email:
                user.email_confirmed = False
                email.send_confirmation_email()
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
        return render(request, 'main/home.html', {'message':'Settings saved successfully!'})
    else:
        return render(request, 'accounts/settings.html', {'provinces':provs})
