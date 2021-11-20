# RoomScout
## The site has been taken down as a result of covid-19 and facebooks new roommate features in marketplace.

![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m784203990-c834dc98966ff65040c545a5)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/xNovax/RoomScout/?ref=repository-badge)

[RoomScout](https://www.roomscout.ca) is a one stop shop for finding and managing roommates


## Setup
1. Download repo
2. Install pip requirements using ``` pip install -r requirements.txt```
3. Setup environment variables
4. Start django local server using ``` python manage.py runserver```

## Environment Variables
Settings for the application are now loaded from environment variables even in development environment, you can also use a local_settings.py file to load settings easier.
An example of this file format is in __Resources__ folder
```
SECRET_KEY : Required
GOOGLE_API_KEY : Optional for google maps
RECAPTCHA_PUBLIC_KEY : Optional for captcha
RECAPTCHA_PRIVATE_KEY : Optional for captcha
AWS_ACCESS_KEY_ID : Optional for S3 Storage and Rekognition
AWS_SECRET_ACCESS_KEY : Optional for S3 Storage and Rekognition
WALK_SCORE_API : Optional for Walk Score
EMAIL_HOST : Optional for email
EMAIL_HOST_USER : Optional for email
EMAIL_HOST_PASSWORD : Optional for email
STRIPE_KEY : Optional for stripe transactions
STRIPE_SECRET_KEY : Optional for stripe transactions

```
    
## Branches
#### Master
    https://roomscout.ca
    Deploys directly to production upon commit
#### Dev
    https://roomscout-dev.herokuapp.com
    Deploys directly to development server

#### All Other
    Any other branch should be a feature branch
    All feature branches should make pull requests into dev and then once approved the dev branch will be merged to master
    
## Testing
All code that is pushed should have tests included for it, if tests are not present it is something that can be done by anyone
#### Forms


#### Views
This is the basic format that tests for views should follow

```
def test_FUNCTION_get(self):
	print('Testing FUNCTION() GET')
	self.client.force_login(self.user)


def test_FUNCTION_get_not_logged_in(self):
	print('Testing FUNCTION() GET not logged in')
	self.client.logout()


def test_FUNCTION_get_wrong_user(self):
	print('Testing FUNCTION() GET wrong user')
	self.client.force_login(self.user2)


def test_FUNCTION_post(self):
	print('Testing FUNCTION() POST')
	self.client.force_login(self.user)


def test_FUNCTION_post_not_logged_in(self):
	print('Testing FUNCTION() POST not logged in')
	self.client.logout()


def test_FUNCTION_post_wrong_user(self):
	print('Testing FUNCTION() POST wrong user}')
	self.client.force_login(self.user2)
```
#### Models

