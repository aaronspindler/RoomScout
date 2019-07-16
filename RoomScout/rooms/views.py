from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.forms.utils import ErrorList
from .models import Room

class room_create(LoginRequiredMixin, generic.CreateView):
    model = Room
    fields = []
    template_name = 'rooms/room_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(room_create, self).form_valid(form)
        return redirect('home')

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
