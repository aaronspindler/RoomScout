import requests
from django.shortcuts import render


def dog(request):
    image = get_dog_image()
    return render(request, 'eggs/dog.html', {'image': image})


def get_dog_image():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    if response.json()['status'] == 'success':
        image = response.json()['message']
        return image
    else:
        return None
