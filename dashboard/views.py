from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from houses.models import House, Invitation
from rooms.models import Inquiry


@login_required(login_url="account_login")
def main_dashboard(request):
    GOOGLE_API_KEY = settings.GOOGLE_API_KEY
    try:
        houses = House.objects.filter(user=request.user)
        member_of_houses = House.objects.filter(members=request.user)
        invitations = Invitation.objects.filter(target=request.user.email)
        inquiries_received = Inquiry.objects.filter(room__house__user=request.user).filter(status='O')
        return render(request, 'dashboard/main_dashboard.html', {'houses': houses, 'member_of_houses': member_of_houses, 'invitations': invitations, 'inquiries_received': inquiries_received, 'GOOGLE_API_KEY': GOOGLE_API_KEY})
    except Exception:
        pass
    return render(request, 'dashboard/main_dashboard.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})
