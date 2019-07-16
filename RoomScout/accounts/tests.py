from django.test import TestCase
from .models import User

class LoginTest(TestCase):
    def test_login_view(self):
        print('Testing accounts.views.login')
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_form_post(self):
        # Create user to login
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'LoginTest', 'email':'Login@test.com', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(pre_count+1, post_count)

        print('Testing accounts.views.login POST : Invalid username/password')
        response = self.client.post('/login',{'username':'asdf1234','password':'asdf1234'})
        self.assertEqual(response.status_code, 200)

        print('Testing accounts.views.login POST : Correct username/password')
        response = self.client.post('/login',{'username':'LoginTest','password':'django1234'})
        self.assertEqual(response.status_code, 302)


class SignupTest(TestCase):

    def test_signup_view(self):
        print('Testing accounts.views.signup')
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)


    def test_signup_form_post_invalid(self):
        print('Testing accounts.views.signup POST Invalid : Form Empty')
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name': '', 'last_name': '', 'username': '', 'email': '', 'password1': '', 'password2': '', 'address': '', 'city': '', 'postal_code': ''})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pre_count, post_count)

        print('Testing accounts.views.signup POST Invalid : Empty Username')
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'', 'email':'testing@1234.com', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pre_count, post_count)

        print('Testing accounts.views.signup POST Invalid :  Empty Email')
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'xNovax123', 'email':'', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pre_count, post_count)

        print('Testing accounts.views.signup POST Invalid :  Empty First Name')
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'', 'last_name':'Spindler', 'username':'xNovax1234', 'email':'testing@test.com', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pre_count, post_count)

        print('Testing accounts.views.signup POST Invalid :  Empty Last Name')
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'', 'username':'xNovax123469', 'email':'testing69@test.com', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pre_count, post_count)


    def test_signup_form_post_repeat(self):
        print('Testing accounts.views.signup POST : User Creation')
        #Create a user
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'xNovax', 'email':'aaron@xnovax.net', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        post_count = User.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(pre_count+1, post_count)

        print('Testing accounts.views.signup POST : Repeat Username')
        #Repeat user by username, shouldn't create another user
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'xNovax', 'email':'aaron@xnovax.net', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        self.assertEqual(response.status_code, 200)
        post_count = User.objects.count()
        self.assertEqual(pre_count, post_count)

        print('Testing accounts.views.signup POST : Repeat Email')
        #Repeat user by email, shouldn't create another user
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'xNova1104x', 'email':'aaron@xnovax.net', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        self.assertEqual(response.status_code, 200)
        post_count = User.objects.count()
        self.assertEqual(pre_count, post_count)

        print('Testing accounts.views.signup POST : User Creation 2')
        #Create a user 2
        pre_count = User.objects.count()
        response = self.client.post('/signup',{'first_name':'Aaron', 'last_name':'Spindler', 'username':'xNova1104x', 'email':'nova1104@live.com', 'password1':'django1234', 'password2':'django1234', 'address':'1234 Main St', 'city':'Vancouver', 'province':'ON', 'postal_code':'K7M 0M4'})
        self.assertEqual(response.status_code, 302)
        post_count = User.objects.count()
        self.assertEqual(pre_count+1, post_count)
