import stripe
from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'main/home.html')
