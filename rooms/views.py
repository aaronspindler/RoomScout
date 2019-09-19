from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from houses.models import House
from .models import Room
from utils.models import RoomImage
from .forms import FilterForm
from utils.captcha import Captcha

def room_list(request):
	filter_form = FilterForm()
	if request.method == 'POST':
		filter_form = FilterForm(request.POST)
		search_term = request.POST['search']
		if filter_form.is_valid():
			results = room_search_extended(
				search_term=search_term,
				max_price=filter_form.cleaned_data['max_price'],
				pets_allowed=filter_form.cleaned_data['pets_allowed'],
				#num_rooms=filter_form.cleaned_data['num_rooms'],
				#num_bathrooms=filter_form.cleaned_data['num_bathrooms'],
				#num_parking_spaces=filter_form.cleaned_data['num_parking_spaces'],
				#has_dishwasher=filter_form.cleaned_data['has_dishwasher'],
				#has_laundry=filter_form.cleaned_data['has_laundry'],
				#has_air_conditioning=filter_form.cleaned_data['has_air_conditioning'],
			)
			rooms = results
		else:
			results = room_search(search_term)
			rooms = results

	else:
		search_term=''
		rooms = Room.objects.filter(is_available=True)
	return render(request, 'rooms/room_list.html', {'rooms':rooms, 'filter_form':filter_form, 'search_term':search_term})

# TODO : Improve search functionality
def room_search(search_term):
	rooms_query = Room.objects.all().filter(is_available=True).filter(Q(house__city__icontains=search_term) | Q(house__prov_state__icontains=search_term) | Q(house__street_name__icontains=search_term))
	return rooms_query

def room_search_extended(search_term, max_price, pets_allowed):#, num_rooms, num_bathrooms, num_parking_spaces, has_dishwasher, has_laundry, has_air_conditioning):
	rooms = Room.objects.all().filter(is_available=True).filter(Q(house__city__icontains=search_term) | Q(house__prov_state__icontains=search_term) | Q(house__street_name__icontains=search_term))
	if(max_price):
		rooms = rooms.filter(price__lte=max_price)
	if(pets_allowed):
		rooms = rooms.filter(house__pets_allowed=True)
	#if(num_rooms):
		#rooms = rooms.filter(house__num_rooms=num_rooms)
	#if(num_bathrooms):
		#rooms = rooms.filter(house__num_rooms__gte=num_rooms)


	return rooms


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

#PK is for the primary key of the photo that is getting deleted
@login_required(login_url="account_login")
def room_delete_photo(request, pk):
	photo = get_object_or_404(RoomImage, pk=pk)
	if photo.user != request.user:
		return Http404
	room = photo.room
	photo.delete()
	return redirect('room_edit', room.pk)

@login_required(login_url="account_login")
def room_inquire(request, pk):
	captcha = Captcha()
	if request.method == 'POST':
		print(request.POST)
	room = get_object_or_404(Room, pk=pk)
	return render(request, 'rooms/room_inquire.html', {'room':room, 'captcha':captcha})

