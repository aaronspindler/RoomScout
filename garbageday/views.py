from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from garbageday.models import GarbageDay
from houses.models import House


@login_required(login_url="account_login")
def garbageday_manage(request, house):
    housemodel = get_object_or_404(House, pk=house)
    if request.user != housemodel.user:
        raise Http404
    garbageday = GarbageDay.objects.filter(house=housemodel)
    if garbageday.count() == 0:
        return redirect('garbageday_create', house=house)
    else:
        return redirect('garbageday_edit', house=house)


@login_required(login_url="account_login")
def garbageday_create(request, house):
    housemodel = get_object_or_404(House, pk=house)
    if request.user != housemodel.user:
        raise Http404
    if housemodel.garbageday_set.count() > 0:
        return redirect(housemodel.get_absolute_url())

    if request.method == 'POST':
        garbageday = GarbageDay()
        garbageday.user = request.user
        garbageday.house = housemodel
        garbageday.last_garbage_day = request.POST['LastGarbageDay']
        garbageday.next_garbage_day = request.POST['NextGarbageDay']
        garbageday.save()
        return redirect(housemodel.get_absolute_url())
    else:
        return render(request, 'garbageday/garbageday_create.html', {'house': housemodel})


@login_required(login_url="account_login")
def garbageday_edit(request, house):
    housemodel = get_object_or_404(House, pk=house)
    garbageday = housemodel.garbageday_set.first()
    if request.user != housemodel.user:
        raise Http404
    if request.method == 'POST':
        garbageday.last_garbage_day = request.POST['LastGarbageDay']
        garbageday.next_garbage_day = request.POST['NextGarbageDay']
        garbageday.save()
        return redirect(housemodel.get_absolute_url())
    else:
        return render(request, 'garbageday/garbageday_edit.html', {'house': housemodel, 'garbageday': garbageday})
