from django.shortcuts import render


def marketing_roommates(request):
	return render(request, 'marketing/roommates.html')
