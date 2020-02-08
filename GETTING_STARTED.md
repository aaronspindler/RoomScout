# Getting Started Guide
This guide is to help you setup RoomScout locally on your computer without hassles, so that you can start contributing to this project as fast as possible. 

# **SETUP/INSTALLATION.**
## Prerequisites
To work with RoomScout you need to have some few prerequisites.

- Python3

- pip

- Virtual environment (virtualenv)

- Code/text editor

- Terminal

- You will also need python installed and knowledge of python


# Forking the Repo 
1. To get to use **RoomScout** first you need to get to the RoomScout repository. 

Link:-> ```https://github.com/xNovax/RoomScout```

2. From there you can access RoomScout App.

3. **Clone** the project.(There are many tutorials online on how to clone a github project).

4. Once you are done with cloning and the project is on your device.

5. Get into project folder (cd into project).

6. Installing Django and other Modules

    `pip install Django`
    `pip install -r requirements.txt`

7. On your **bash** terminal Run the command:- 

run: 
* $ python manage.py runserver

- At this point you should get some errors caused by environment variables not set. To fix this, you need to modify your settings.py file for local server development. 
- Also, you need to setup a local Database (e.g, PostgreSql) that will work for the App locally.


## Environment Variables and Settings
- For the environment variables, you need to edit the settings file and remove the `os.environ` part and replace it with some values for the secret key and/or enter empty strings for the other optional variables. 

- You can also use a local_settings.py file to load settings easier.
An example of this file format is in __Resources__ folder. Check the resource folder for a sample settings file that you can copy and use. 

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

# Contributing
- If you would like to contribute to Roomscout.ca, please take a look at the [current issues](https://github.com/xNovax/RoomScout/issues). If there is a bug or feature that you want but it isn't listed, make an issue and work on it.

- For you to contribute, you need to create a branch on your computer from the `master` branch and checkout into this branch. This feature branch is where you will write your own codes and modify the application. 


## Branches
#### Master
    https://roomscout.ca
    Deploys directly to production upon commit
#### Dev
    https://roomscout-dev.herokuapp.com
    Deploys directly to development server

#### All Other
    Any other branch should be a feature branch
    All feature branches should make pull requests into dev and then once approved the dev branch will be merged to master. 
**Don't make a pull request to the master branch, use dev branch**


# Creating a Pull Request 
- After you are done make your contributions on your local branch, then git commit and git push `that branch` to your github repository. 

- After you have pushed from your local to github, open your web browser and go to the forked RoomScout repo on your account. 

- At the top of the forked repo, you should see a notice asking you to create a pull request, click the `pull request` button and choose the `dev` branch to merge with your newly pushed feature branch. (Default branch will be master, so you need to change it to dev)

# Getting Approved!
After creating a pull request, the maintainers will be notified and they will review your codes and merge it with the dev branch. 


## Testing
All code that is pushed should have tests included for it, if tests are not present it is something that can be done by anyone


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

