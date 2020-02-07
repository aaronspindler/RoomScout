# Getting Started Guide
This guide is to help you setup RoomScout locally on your computer without hassles, so that you can start contributing to this project as fast as possible. 

# **SETUP/INSTALLATION.**
## Prerequisites
To work with RoomScout you need to have some few prerequisites.

- Python3+

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
