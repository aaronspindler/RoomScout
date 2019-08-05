from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from houses.models import House
from .models import Room


@login_required(login_url="/login")
def room_create(request):
	if request.method == 'POST':
		print(request.POST)
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
