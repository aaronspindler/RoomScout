from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404, render

from .models import Bill, BillSet


# PK is the primary key for the bill
@login_required(login_url="account_login")
def bill_delete(request, pk):
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


# PK is the primary key for the bill
def bill_add_file(request, pk):
	bill = get_object_or_404(Bill, pk=pk)
	house = bill.set.house

	if request.method == 'POST':
		pass

	return render(request, 'bills/bill_add_file.html', {'house': house})
