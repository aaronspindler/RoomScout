from .models import IP
def collectIP(request, user):
	newIP = IP()
	newIP.ip_address = request.META.get('REMOTE_ADDR')
	newIP.user = user
	newIP.save()