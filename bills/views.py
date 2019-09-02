# Create your views here.
from django.shortcuts import redirect

# PK is the primary key for the billset that this bill needs to belong to
def bill_add(request, pk):
	print(pk)
	return redirect('main_dashboard')