from django.conf import settings
from django.core.files import File
from .models import HouseImage
import urllib.request


def load_house_image(house):
	try:
		url = 'https://maps.googleapis.com/maps/api/streetview?size=640x480&location={},{}&key={}'.format(house.lat, house.lon, settings.GOOGLE_API_KEY)
		data = urllib.request.urlretrieve(url)
		image = HouseImage()
		image.user = house.user
		image.house = house
		image.image.save('houseimage.png', File(open(data[0], 'rb')))
		image.save()
	except Exception:
		pass
