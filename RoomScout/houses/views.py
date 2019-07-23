from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView
from django.forms.utils import ErrorList
from .models import House
from .forms import HouseForm
from utils.datetime import now

@login_required(login_url="/login")
def house_create(request):
    form = HouseForm()

    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = House()
            house.user = request.user
            house.date_posted = now()
            house.address = form.cleaned_data['address']
            house.country = form.cleaned_data['country']
            house.prov_state = form.cleaned_data['prov_state']
            house.postal_code = form.cleaned_data['postal_code']
            house.save()
            return redirect('home')
    else:
        return render(request, 'houses/house_create.html', {'form': form})


class house_detail(generic.DetailView):
    model = House
    template_name = 'houses/house_detail.html'

class house_edit(LoginRequiredMixin, generic.UpdateView):
    model = House
    template_name = 'houses/house_edit.html'
    fields = ['title']
    success_url = reverse_lazy('home')

    def get_object(self):
        hall = super(UpdateHall, self).get_object()
        if not hall.user == self.request.user:
            raise Http404
        return hall

class house_delete(LoginRequiredMixin, generic.DeleteView):
    model = House
    template_name = 'houses/house_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        hall = super(DeleteHall, self).get_object()
        if not hall.user == self.request.user:
            raise Http404
        return hall
