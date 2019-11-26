import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from bills.models import BillSet, Bill
from rooms.models import Room
from utils.captcha import Captcha
from utils.datetime import now
from emails.senders import send_invite_email, send_bill_email
from utils.models import RoomImage, BillFile
from utils.date import check_format
from utils.streetview import load_house_image
from .models import House, Invitation


@login_required(login_url="account_login")
def house_create(request):
    captcha = Captcha()
    GOOGLE_API_KEY = settings.GOOGLE_API_KEY
    if request.method == 'POST':
        house = House()
        house.user = request.user
        if request.POST['street_number'] and request.POST['street_number'] and request.POST['street_name'] and \
                request.POST['city'] and request.POST['prov_state'] and request.POST['country']:
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

            init_bill_set = BillSet()

            date = now()
            init_bill_set.month = date.month
            init_bill_set.year = date.year
            init_bill_set.house = house
            init_bill_set.save()

            house.load_walk_score()

            #Todo : Put this in a celery task to be done in queue
            load_house_image(house)

            return redirect('house_detail', pk=house.id)
        return render(request, 'houses/house_create.html',
                      {'error': 'There is an issue with the address inputted!', 'GOOGLE_API_KEY': GOOGLE_API_KEY,
                       'captcha': captcha})
    else:
        return render(request, 'houses/house_create.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY, 'captcha': captcha})


@login_required(login_url="account_login")
def house_bill_add(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.user.id != house.user.id:
        raise Http404

    if request.method == 'POST':
        bill = Bill()
        bill.user = request.user
        if request.POST['type'] == '' or request.POST['date'] == '' or request.POST['amount'] == '':
            return render(request, 'houses/house_bill_add.html',
                          {'house': house, 'error': 'You have entered invalid data!'})

        bill.type = request.POST['type']
        bill.date = request.POST['date']
        bill.amount = request.POST['amount']

        date = request.POST['date']

        if not check_format(date):
            return render(request, 'houses/house_bill_add.html',
                          {'house': house, 'error': 'You have enter the date in an incorrect format! Use yyyy-mm-dd'})

        parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        month = parsed_date.month
        year = parsed_date.year

        existing_billset = BillSet.objects.filter(house=house).filter(year=year).filter(month=month)
        if (existing_billset.count() == 0):
            new_billset = BillSet()
            new_billset.house = house
            new_billset.month = month
            new_billset.year = year
            new_billset.save()
            bill.set = new_billset
        else:
            bill.set = existing_billset.first()
        bill.save()

        if len(request.FILES) > 0:
            billfile = BillFile()
            billfile.user = request.user
            billfile.file = request.FILES['file']
            billfile.bill = bill
            billfile.save()

        send_bill_email(house, bill)
        return redirect('house_detail', house.pk)

    return render(request, 'houses/house_bill_add.html', {'house': house})


@login_required(login_url="account_login")
def house_invite(request, pk):
    house = get_object_or_404(House, pk=pk)
    if (request.user.id != house.user.id):
        raise Http404
    captcha = Captcha()
    if (request.method == 'POST'):
        if (request.POST['email'] != ''):
            invitation = Invitation()
            invitation.house = house
            invitation.sender = request.user
            invitation.target = request.POST['email']
            invitation.save()
            send_invite_email(request.POST['email'], invitation)

        return redirect('house_detail', pk=pk)
    return render(request, 'houses/house_invite.html', {'house': house, 'captcha': captcha})


@login_required(login_url="account_login")
def house_invite_remove(request, pk, id):
    house = get_object_or_404(House, pk=pk)
    if (request.user.id != house.user.id):
        raise Http404
    invite = get_object_or_404(Invitation, id=id)
    invite.delete()
    return redirect('house_detail', pk=pk)


@login_required(login_url="account_login")
def house_invite_accept(request, pk, id):
    house = get_object_or_404(House, pk=pk)
    invite = get_object_or_404(Invitation, id=id)
    if (request.user.email != invite.target):
        raise Http404

    house.members.add(request.user)
    invite.delete()
    return redirect('house_detail', pk=pk)


@login_required(login_url="account_login")
def house_invite_decline(request, pk, id):
    invite = get_object_or_404(Invitation, id=id)
    if (request.user.email != invite.target):
        raise Http404
    invite.delete()
    return redirect('main_dashboard')


@login_required(login_url="account_login")
def house_member_remove(request, pk, id):
    house = get_object_or_404(House, pk=pk)
    if (request.user.id != house.user.id):
        raise Http404
    member = house.members.filter(id=id).first()
    house.members.remove(member)
    return redirect('house_detail', pk=pk)


@login_required(login_url="account_login")
def house_add_room(request, pk):
    house = House.objects.filter(pk=pk).get()
    if (house.user != request.user):
        raise Http404
    if (request.method == 'POST'):
        room = Room()
        room.user = request.user
        room.name = request.POST['name']
        room.house = house
        room.price = request.POST['price']
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

    return render(request, 'houses/room_add.html', {'house': house})


def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    GOOGLE_API_KEY = settings.GOOGLE_API_KEY
    is_member = False
    if request.user in house.members.all():
        is_member = True
    if request.user.id == house.user.id:
        is_member = True

    try:
        rooms = Room.objects.filter(house=house)
        return render(request, 'houses/house_detail.html', {'rooms': rooms, 'house': house, 'is_member': is_member, 'GOOGLE_API_KEY': GOOGLE_API_KEY})
    except Exception:
        pass

    return render(request, 'houses/house_detail.html',
                  {'house': house, 'is_member': is_member, 'GOOGLE_API_KEY': GOOGLE_API_KEY})


class house_edit(LoginRequiredMixin, generic.UpdateView):
    model = House
    template_name = 'houses/house_edit.html'
    fields = ['hide_address', 'num_rooms', 'num_bathrooms', 'num_parking_spaces', 'has_dishwasher', 'has_laundry',
              'has_air_conditioning']

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
    success_url = reverse_lazy('main_dashboard')

    def get_object(self):
        house = super(house_delete, self).get_object()
        if not house.user == self.request.user:
            raise Http404
        return house
