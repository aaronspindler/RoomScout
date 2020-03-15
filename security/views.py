from django.http import JsonResponse

from .helpers import get_IP
from .models import Fingerprint, IP


def fingerprint_save(request):
    if request.method == 'POST':
        if request.POST['murmur']:
            user = request.user
            ip_address = get_IP(request)

            if user.is_anonymous:
                ip = IP()
                ip.address = ip_address
                ip.save()
                fingerprint = Fingerprint(hash=request.POST['murmur'], ip=ip).save()
            else:
                ip = IP()
                ip.address = ip_address
                ip.user = user
                ip.save()
                fingerprint = Fingerprint(hash=request.POST['murmur'], user=user, ip=ip).save()

            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})
