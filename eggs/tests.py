from django.test import TestCase
from django.urls import reverse

from .views import get_dog_image


class EggsTests(TestCase):
    def test_dog_view(self):
        print("Testing eggs.views.dog()")
        response = self.client.get(reverse('ee_dog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for your kind donation')
        self.assertNotContains(response, 'This should not be contained!')
        self.assertTemplateUsed(response, 'eggs/dog.html')

    def test_get_dog_image(self):
        print("Testing eggs.views.get_dog_image()")
        image1 = get_dog_image()
        self.assertIsNotNone(image1)
        image2 = get_dog_image()
        self.assertNotEqual(image1, image2)
