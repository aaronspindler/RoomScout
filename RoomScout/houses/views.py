from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings

from .forms import SearchForm
from .models import House


@login_required(login_url="/login")
def house_create(request):
	GOOGLE_API_KEY = settings.GOOGLE_API_KEY
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			#house = House()
			#house.save()
			#return redirect('house_detail', pk=house.id)
			pass
	else:
		return render(request, 'houses/house_create.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})


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
