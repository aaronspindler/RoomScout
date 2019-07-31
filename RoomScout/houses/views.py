from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import House
from rooms.models import Room


@login_required(login_url="/login")
def house_create(request):
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	if request.method == 'POST':
		if len(request.POST) < 7 or len(request.POST) > 7:
			return render(request, 'houses/house_create.html',
			              {'error': 'There is an issue with the address inputted!', 'GOOGLE_API_KEY': GOOGLE_API_KEY})
		house = House()
		house.user = request.user
		if request.POST['street_number'] and request.POST['street_number'] and request.POST['street_name'] and \
				request.POST['city'] and request.POST['prov_state'] and request.POST['postal_code'] and request.POST[
			'country']:
			house.street_number = request.POST['street_number']
			house.street_name = request.POST['street_name']
			house.city = request.POST['city']
			house.prov_state = request.POST['prov_state']
			house.postal_code = request.POST['postal_code']
			house.country = request.POST['country']
			house.save()
			return redirect('house_detail', pk=house.id)
		return render(request, 'houses/house_create.html',
		              {'error': 'There is an issue with the address inputted!', 'GOOGLE_API_KEY': GOOGLE_API_KEY})
	else:
		return render(request, 'houses/house_create.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})


def house_detail(request, pk):
	house = get_object_or_404(House, pk=pk)
	try:
		rooms = Room.objects.filter(house=house)
		return render(request, 'houses/house_detail.html', {'rooms':rooms, 'house':house})
	except Exception:
		pass

	return render(request,'houses/house_detail.html', {'house':house})


class house_edit(LoginRequiredMixin, generic.UpdateView):
	model = House
	template_name = 'houses/house_edit.html'
	fields = ['is_approved', 'hide_address']
	success_url = reverse_lazy('home')

	def get_object(self):
		house = super(house_edit, self).get_object()
		if not house.user == self.request.user:
			raise Http404
		return house


class house_delete(LoginRequiredMixin, generic.DeleteView):
	model = House
	template_name = 'houses/house_delete.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		house = super(house_edit, self).get_object()
		if not house.user == self.request.user:
			raise Http404
		return house
