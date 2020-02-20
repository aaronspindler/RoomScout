def get_IP(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
