# RoomScout
RoomScout is a one stop shop for finding and managing roommates


## Setup
1. Download repo
2. Install pip requirements using ``` pip install -r requirements.txt```
3. Setup environment variables
4. Start django local server using ``` python manage.py runserver```

## Environment Variables
    Settings for the application are now loaded from environment variables even in development environment

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

