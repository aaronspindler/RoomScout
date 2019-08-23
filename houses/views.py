from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from accounts.models import User
from rooms.models import Room
from utils.models import RoomImage
from .models import House, Invitation


@login_required(login_url="account_login")
def house_create(request):
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	if request.method == 'POST':
		house = House()
		house.user = request.user
		if request.POST['street_number'] and request.POST['street_number'] and request.POST['street_name'] and \
				request.POST['city'] and request.POST['prov_state'] and request.POST[
			'country']:
			house.street_number = request.POST['street_number']
			house.street_name = request.POST['street_name']
			house.city = request.POST['city']
			house.prov_state = request.POST['prov_state']
			house.postal_code = request.POST['postal_code']
			house.country = request.POST['country']
			house.place_id = request.POST['place_id']
			house.lat = request.POST['lat']
			house.lon = request.POST['lon']
			house.save()
			house.load_walk_score()
			return redirect('house_detail', pk=house.id)
		return render(request, 'houses/house_create.html', {'error': 'There is an issue with the address inputted!', 'GOOGLE_API_KEY': GOOGLE_API_KEY})
	else:
		return render(request, 'houses/house_create.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})

@login_required(login_url="account_login")
def house_invite(request, pk):
	house = get_object_or_404(House, pk=pk)
	if (request.user.id != house.user.id):
		return Http404

	if(request.method == 'POST'):
		if(request.POST['email'] != ''):
			users = User.objects.filter(Q(email__iexact=request.POST['email']))
			#If users == 0 then the user is not signed up
			#Send a email telling them they've been invited to a house and should signup
			if(users.count() == 0):
				print('user not found')
				invitation = Invitation()
				invitation.house = house
				invitation.sender = request.user
				invitation.target = request.POST['email']
				invitation.save()
			# Else user already has an account and an invitation should be created and put on their dashboard
			else:
				print(users)
		return redirect('house_detail', pk=pk)
	return render(request, 'houses/house_invite.html', {'house':house})

@login_required(login_url="account_login")
def house_invite_remove(request, pk, id):
	house = get_object_or_404(House, pk=pk)
	if (request.user.id != house.user.id):
		return Http404
	invite = get_object_or_404(Invitation, id=id)
	invite.delete()
	return redirect('house_detail', pk=pk)

@login_required(login_url="account_login")
def house_member_remove(request, pk, id):
	house = get_object_or_404(House, pk=pk)
	if (request.user.id != house.user.id):
		return Http404
	member = house.members.filter(id=id).first()
	house.members.remove(member)
	return redirect('house_detail', pk=pk)

@login_required(login_url="account_login")
def house_list(request):
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	try:
		houses = House.objects.filter(user=request.user)
		return render(request, 'houses/house_list.html', {'houses':houses,'GOOGLE_API_KEY': GOOGLE_API_KEY})
	except Exception:
		pass
	return render(request, 'houses/house_list.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})

@login_required(login_url="account_login")
def house_add_room(request, pk):
	house = House.objects.filter(pk=pk).get()
	if(house.user != request.user):
		return Http404
	if(request.method == 'POST'):
		room = Room()
		room.user = request.user
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

	return render(request, 'houses/room_add.html', {'house': house})

def house_detail(request, pk):
	house = get_object_or_404(House, pk=pk)
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	is_member = False
	if request.user in house.members.all():
		is_member = True
	if request.user.id == house.user.id:
		is_member= True

	try:
		rooms = Room.objects.filter(house=house)
		return render(request, 'houses/house_detail.html', {'rooms':rooms, 'house':house, 'is_member':is_member, 'GOOGLE_API_KEY': GOOGLE_API_KEY})
	except Exception:
		pass

	return render(request,'houses/house_detail.html', {'house':house, 'is_member':is_member, 'GOOGLE_API_KEY': GOOGLE_API_KEY})


class house_edit(LoginRequiredMixin, generic.UpdateView):
	model = House
	template_name = 'houses/house_edit.html'
	fields = ['postal_code', 'hide_address']

	def get_success_url(self):
		return reverse('house_detail', kwargs={'pk': self.object.pk})

	def get_object(self):
		house = super(house_edit, self).get_object()
		if not house.user == self.request.user:
			raise Http404
		return house


class house_delete(LoginRequiredMixin, generic.DeleteView):
	model = House
	template_name = 'houses/house_delete.html'
	success_url = reverse_lazy('house_list')

	def get_object(self):
		house = super(house_delete, self).get_object()
		if not house.user == self.request.user:
			raise Http404
		return house
