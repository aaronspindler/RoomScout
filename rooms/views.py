from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from houses.models import House
from utils.captcha import Captcha
from emails.senders import send_inquiry_email
from utils.models import RoomImage
from .forms import FilterForm
from .models import Room, Inquiry, RoomLike


def room_list(request):
    filter_form = FilterForm()
    if request.method == 'POST':
        filter_form = FilterForm(request.POST)
        search_term = request.POST['search']
        if filter_form.is_valid():
            results = room_search_extended(
                search_term=search_term,
                max_price=filter_form.cleaned_data['max_price'],
                pet_friendly=filter_form.cleaned_data['pet_friendly'],
                has_dishwasher=filter_form.cleaned_data['has_dishwasher'],
                has_laundry=filter_form.cleaned_data['has_laundry'],
                has_air_conditioning=filter_form.cleaned_data['has_air_conditioning'],
                open_to_students=filter_form.cleaned_data['open_to_students'],
                is_accessible=filter_form.cleaned_data['is_accessible'],
                utilities_included=filter_form.cleaned_data['utilities_included']
            )
            rooms = results.order_by(filter_form['order_by'].value())
        else:
            # By default, show newest first
            results = room_search(search_term)
            rooms = results.order_by('-updated_at')

    else:
        search_term = ''
        rooms = Room.objects.filter(is_available=True).order_by('-updated_at')
    saved_rooms = get_saved_rooms(request)
    return render(request, 'rooms/room_list.html', {'rooms': rooms, 'saved_rooms': saved_rooms, 'filter_form': filter_form, 'search_term': search_term})


@login_required(login_url="account_login")
def room_saved(request):
    saved_rooms = RoomLike.objects.filter(user=request.user)
    return render(request, "rooms/room_saved.html", {'saved_rooms': saved_rooms})


# TODO Make this view only affect system state when they are POST requests
# PK is the primary key for the room
@login_required(login_url="account_login")
def room_like(request, pk):
    user = request.user
    room = get_object_or_404(Room, pk=pk)
    roomlike = RoomLike.objects.filter(user=user, room=room)

    if roomlike.count() == 0:
        new_room_like = RoomLike()
        new_room_like.user = user
        new_room_like.room = room
        new_room_like.save()

    return JsonResponse({'status': 'success'})

# TODO Make this view only affect system state when they are POST requests
# PK is the primary key for the room
@login_required(login_url="account_login")
def room_unlike(request, pk):
    user = request.user
    room = get_object_or_404(Room, pk=pk)
    roomlikes = RoomLike.objects.filter(user=user, room=room)
    if roomlikes.count() == 0:
        return JsonResponse({'status': 'failure'})
    roomlike = roomlikes.first()
    roomlike.delete()

    return JsonResponse({'status': 'success'})


# TODO : Improve search functionality
def room_search(search_term):
    rooms_query = Room.objects.all().filter(is_available=True).filter(
        Q(house__city__icontains=search_term) | Q(house__prov_state__icontains=search_term) | Q(
            house__street_name__icontains=search_term))
    return rooms_query


def room_search_extended(search_term, max_price, pet_friendly, has_dishwasher, has_laundry, has_air_conditioning,
                         open_to_students, is_accessible, utilities_included):
    rooms = Room.objects.all().filter(is_available=True).filter(
        Q(house__city__icontains=search_term) | Q(house__prov_state__icontains=search_term) | Q(
            house__street_name__icontains=search_term))
    if (max_price):
        rooms = rooms.filter(price__lte=max_price)
    if (pet_friendly):
        rooms = rooms.filter(pet_friendly=True)
    if (has_dishwasher):
        rooms = rooms.filter(Q(house__has_dishwasher=True))
    if (has_laundry):
        rooms = rooms.filter(Q(house__has_laundry=True))
    if (has_air_conditioning):
        rooms = rooms.filter(Q(house__has_air_conditioning=True))
    if (open_to_students):
        rooms = rooms.filter(open_to_students=True)
    if (is_accessible):
        rooms = rooms.filter(is_accessible=True)
    if (utilities_included):
        rooms = rooms.filter(utilities_included=True)
    return rooms


@login_required(login_url="account_login")
def room_create(request):
    if request.method == 'POST':
        if request.POST['house'] and request.POST['name'] and request.POST['price']:
            room = Room()
            room.user = request.user
            house = House.objects.filter(pk=request.POST['house'])[:1].get()
            room.house = house
            if 'name' not in request.POST:
                return render(request, 'houses/room_add.html', {'house': house, 'error': 'Please make sure to fill in all required details'})
            else:
                room.name = request.POST['name']

            if 'price' not in request.POST:
                return render(request, 'houses/room_add.html', {'house': house, 'error': 'Please make sure to fill in all required details'})
            else:
                room.price = request.POST['price']

            if 'description' not in request.POST:
                return render(request, 'houses/room_add.html', {'house': house, 'error': 'Please make sure to fill in all required details'})
            else:
                room.description = request.POST['description']
            room.save()
            try:
                for file in request.FILES.getlist('images'):
                    image = RoomImage()
                    image.room = room
                    image.user = request.user
                    image.image = file
                    image.save()
            except Exception:
                pass

        return redirect('room_detail', pk=room.id)
    else:
        houses = House.objects.filter(user=request.user.id)
        if houses.count() > 0:
            return render(request, 'rooms/room_create.html', {'houses': houses})
        else:
            return render(request, 'rooms/room_create.html')


class room_detail(generic.DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'


class room_edit(LoginRequiredMixin, generic.UpdateView):
    model = Room
    template_name = 'rooms/room_edit.html'
    fields = ['name', 'price', 'description', 'is_available', 'furnished', 'is_accessible', 'open_to_students',
              'female_only', 'pet_friendly', 'utilities_included', 'parking']

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
        return render(request, 'rooms/room_add_photo.html', {'room': room})
    raise Http404


# PK is for the primary key of the photo that is getting deleted
@login_required(login_url="account_login")
def room_delete_photo(request, pk):
    photo = get_object_or_404(RoomImage, pk=pk)
    if photo.user != request.user:
        raise Http404
    room = photo.room
    photo.delete()
    return redirect('room_edit', room.pk)


@login_required(login_url="account_login")
def room_inquire(request, pk):
    captcha = Captcha()
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        inquiry = Inquiry()
        inquiry.user = request.user
        inquiry.room = room
        if request.POST['message'] == '':
            return render(request, 'rooms/room_inquire.html', {'room': room, 'captcha': captcha})
        inquiry.message = request.POST['message']
        if request.POST['move_in_date'] != '':
            inquiry.move_in_date = request.POST['move_in_date']
        inquiry.save()
        send_inquiry_email(room.user.email, inquiry)
        messages.success(request, 'Your inquiry has been successfully sent!.')
        return redirect('main_dashboard')

    return render(request, 'rooms/room_inquire.html', {'room': room, 'captcha': captcha})


# pk is the primary key of the inquiry
@login_required(login_url="account_login")
def room_inquire_dismiss(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if inquiry.room.user != request.user:
        raise Http404
    inquiry.status = 'D'
    inquiry.save()
    return redirect('main_dashboard')


def get_saved_rooms(request):
    user = request.user
    if user.id is not None:
        room_likes = RoomLike.objects.all().filter(user=user)
        saved_rooms = []

        for roomlike in room_likes:
            saved_rooms.append(roomlike.room)
        return saved_rooms
    return []
