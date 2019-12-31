import stripe
from django.conf import settings
from django.shortcuts import redirect
from .models import Donation

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_donation(request, amount):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=amount * 100,
            currency='cad',
            description='Donation - ${}'.format(amount),
            source=request.POST['stripeToken']
        )
        
        donation = Donation()
        donation.email = request.POST['stripeEmail']
        donation.amount = amount * 1.00
        donation.save()
        
        return redirect('ee_dog')
    else:
        return redirect('supportus')
