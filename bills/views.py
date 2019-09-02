# Create your views here.
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from .models import Bill, BillSet
from utils.models import BillFile

# PK is the primary key for the billset that this bill needs to belong to
def bill_add(request, pk):
	bill = Bill()
	billset = get_object_or_404(BillSet, pk=pk)
	if request.user != billset.house.user:
		return Http404
	bill.set = billset
	bill.user = request.user
	bill.type = request.POST['type']
	bill.date = request.POST['date']
	bill.amount = request.POST['amount']

	bill.save()

	if len(request.FILES) > 0:
		billfile = BillFile()
		billfile.user = request.user
		billfile.file = request.FILES['file']
		billfile.bill = bill
		billfile.save()

	return redirect('house_detail', billset.house.pk)

# PK is the primary key for the bill
def bill_delete(request, pk):
	bill = get_object_or_404(Bill, pk=pk)
	house = bill.set.house
	if request.user != bill.user:
		return Http404
	bill.delete()
	return redirect('house_detail', house.pk)