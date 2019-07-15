from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django_countries import countries

from .models import User

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email = request.POST['email'])
                    return render(request, 'accounts/signup.html', {'error':'Email is already in use!'})
                except User.DoesNotExist:
                    if request.POST['firstname'] and request.POST['lastname']:
                        email = request.POST['email']
                        username = request.POST['username']
                        password = request.POST['password1']
                        firstname = request.POST['firstname']
                        lastname = request.POST['lastname']
                        if request.POST['address']:
                            address = request.POST['address']
                        else:
                            address = None

                        if request.POST['province']:
                            prov_state = request.POST['province']
                        else:
                            prov_state = None

                        if request.POST['postal_code']:
                            postal_code = request.POST['postal_code']
                        else:
                            postal_code = None

                        user = User.objects.create_user(username, password=password)
                        user.email = email
                        user.firstname = firstname
                        user.lastname = lastname
                        user.address = address
                        user.prov_state = prov_state
                        user.postal_code = postal_code
                        user.score = 0.0
                        user.save()
                        login(request,user)
                        return redirect('home')
                    else:
                        return render(request, 'accounts/signup.html', {'error':'Please enter your first and last name!'})

        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match!'})
    else:
        return render(request, 'accounts/signup.html')

def settings(request):
    return render(request, 'accounts/settings.html')
