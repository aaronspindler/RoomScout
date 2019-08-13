from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from utils import provinces, emailclient
from .models import User

@login_required(login_url="/login")
def settings(request):
	provs = provinces.get_provinces()
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
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
		return redirect('settings')
	else:
		return render(request, 'account/settings.html', {'provinces': provs})
