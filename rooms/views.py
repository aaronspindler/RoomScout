from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from houses.models import House
from .models import Room
from utils.models import RoomImage

def room_list(request):
	rooms = Room.objects.all()
	return render(request, 'rooms/room_list.html', {'rooms':rooms})


@login_required(login_url="account_login")
def room_create(request):
	if request.method == 'POST':
		print(request.POST)
		if request.POST['house'] and request.POST['name'] and request.POST['price']:
			room = Room()
			room.user = request.user
			house = House.objects.filter(pk=request.POST['house'])[:1].get()
			room.name = request.POST['name']
			room.house = house
			room.price = request.POST['price']
			room.save()
			try:
				roomImage = RoomImage()
				roomImage.room = room
				roomImage.user = request.user
				roomImage.image = request.FILES['image']
				roomImage.save()
			except Exception:
				pass

		return redirect('room_detail', pk=room.id)
	else:
		try:
			houses = House.objects.filter(user=request.user.id)
			return render(request, 'rooms/room_create.html', {'houses': houses})
		except Exception:
			pass
		return render(request, 'rooms/room_create.html')


class room_detail(generic.DetailView):
	model = Room
	template_name = 'rooms/room_detail.html'


class room_edit(LoginRequiredMixin, generic.UpdateView):
	model = Room
	template_name = 'rooms/room_edit.html'
	fields = ['name', 'price', 'is_available']
	success_url = reverse_lazy('home')

	def get_object(self):
		room = super(room_edit, self).get_object()
		if not room.user == self.request.user:
			raise Http404
		return room


class room_delete(LoginRequiredMixin, generic.DeleteView):
	model = Room
	template_name = 'rooms/room_delete.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		room = super(room_delete, self).get_object()
		if not room.user == self.request.user:
			raise Http404
		return room
