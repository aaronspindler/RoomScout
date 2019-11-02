from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

from .models import Bill, BillSet

# PK is the primary key for the bill
def bill_delete(request, pk):
	delete_set = False
	bill = get_object_or_404(Bill, pk=pk)
	set_key = bill.set.pk
	house = bill.set.house
	if request.user != bill.user:
		raise Http404

	if Bill.objects.filter(set=bill.set).count() == 1:
		delete_set = True

	bill.delete()

	if delete_set == True:
		BillSet.objects.filter(pk=set_key).delete()

	return redirect('house_detail', house.pk)
