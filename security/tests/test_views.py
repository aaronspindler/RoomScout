from django.contrib.auth import get_user_model
from django.test import TestCase, Client


# TODO: Write tests for security views
class SecurityViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='FredFlintstone', email='aaron@xnovax.net', password='babadoo')
        self.user2 = User.objects.create_user(username='JackyFlintstone', email='jacky@flintstone.com', password='lovefred')
