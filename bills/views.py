from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404, render

from utils.models import BillFile
from .forms import BillFileForm
from .models import Bill, BillSet


@login_required(login_url="account_login")
def bill_delete(request, pk):
	# PK is the primary key for the bill
	delete_set = False
	bill = get_object_or_404(Bill, pk=pk)
	set_key = bill.set.pk
	house = bill.set.house
	if request.user != bill.user:
		raise Http404
	
	if request.method == 'POST':
		if Bill.objects.filter(set=bill.set).count() == 1:
			delete_set = True
	
		bill.delete()
	
		if delete_set:
			BillSet.objects.filter(pk=set_key).delete()
	
	return redirect('house_detail', house.pk)


@login_required(login_url="account_login")
def bill_add_file(request, pk):
	# PK is the primary key for the bill

	bill = get_object_or_404(Bill, pk=pk)
	house = bill.set.house
	form = BillFileForm()

	if request.user != bill.user:
		raise Http404

	if request.method == 'POST':
		form = BillFileForm(request.POST, request.FILES)
		if form.is_valid():
			billfile = BillFile()
			billfile.user = request.user
			billfile.file = form.cleaned_data['file']
			billfile.bill = bill
			billfile.save()
			return redirect(house.get_absolute_url())
		else:
			return render(request, 'bills/bill_add_file.html', {'house': house, 'form': form})
	return render(request, 'bills/bill_add_file.html', {'house': house, 'form': form})
