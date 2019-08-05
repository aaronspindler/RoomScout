from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from houses.models import House
from .models import Room
from utils.models import RoomImage


@login_required(login_url="/login")
def room_create(request):
	if request.method == 'POST':
		print(request.POST)
		if request.POST['house'] and request.POST['name'] and request.FILES['image'] and request.POST['price']:
			room = Room()
			house = House.objects.filter(pk=request.POST['house'])[:1].get()
			room.name = request.POST['name']
			room.house = house
			room.price = request.POST['price']
			room.save()
			roomImage = RoomImage()
			roomImage.room = room
			roomImage.user = request.user
			roomImage.image = request.FILES['image']
			roomImage.save()

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
	fields = ['title']
	success_url = reverse_lazy('home')

	def get_object(self):
		hall = super(UpdateHall, self).get_object()
		if not hall.user == self.request.user:
			raise Http404
		return hall


class room_delete(LoginRequiredMixin, generic.DeleteView):
	model = Room
	template_name = 'rooms/room_delete.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		hall = super(DeleteHall, self).get_object()
		if not hall.user == self.request.user:
			raise Http404
		return hall
