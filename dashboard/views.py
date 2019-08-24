from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from houses.models import House


@login_required(login_url="account_login")
def main_dashboard(request):
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	try:
		houses = House.objects.filter(user=request.user)
		return render(request, 'dashboard/main_dashboard.html', {'houses':houses,'GOOGLE_API_KEY': GOOGLE_API_KEY})
	except Exception:
		pass
	return render(request, 'dashboard/main_dashboard.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})