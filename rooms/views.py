from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
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

	def get_success_url(self):
		return reverse('room_detail', kwargs={'pk': str(self.object.pk)})

	def get_object(self):
		room = super(room_edit, self).get_object()
		if not room.user == self.request.user:
			raise Http404
		return room


class room_delete(LoginRequiredMixin, generic.DeleteView):
	model = Room
	template_name = 'rooms/room_delete.html'
	success_url = reverse_lazy('main_dashboard')

	def get_object(self):
		room = super(room_delete, self).get_object()
		if not room.user == self.request.user:
			raise Http404
		return room

@login_required(login_url="account_login")
def room_add_photo(request, pk):
	room = get_object_or_404(Room, pk=pk)
	if room.user == request.user:
		if request.method == 'POST':
			for file in request.FILES.getlist('files'):
				image = RoomImage()
				image.room = room
				image.user = request.user
				image.image = file
				image.save()

			return redirect('room_detail', pk=room.id)
		return render(request, 'rooms/room_add_photo.html', {'room':room})
	return Http404

def room_search(request):
	search_term = request.GET['search_term']
	print(search_term)
	return JsonResponse({'error': 'Not able to validate form'})