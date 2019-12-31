import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Stripe
STRIPE_KEY = ''
STRIPE_SECRET_KEY = ''

# Google
GOOGLE_API_KEY = ''
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_USE_SSL = True
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.AllauthSignupForm'

# Walk Score
WALK_SCORE_API = ''

# AWS
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_DEFAULT_ACL = None

AWS_PUBLIC_MEDIA_LOCATION = ''
DEFAULT_FILE_STORAGE = 'Roomscout.storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = ''
PRIVATE_FILE_STORAGE = 'Roomscout.storage_backends.PrivateMediaStorage'

AWS_S3_OBJECT_PARAMETERS = {
	'CacheControl': 'max-age=86400',
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Authentication
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'RoomScout.ca | '

AUTHENTICATION_BACKENDS = {
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend'
}

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'main_dashboard'
ACCOUNT_LOGOUT_REDIRECT = 'home'

# Email
DEFAULT_FROM_EMAIL = 'services@roomscout.ca'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
	# Django
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'django.contrib.sites',
	# 3rd Party
	'crispy_forms',
	'django_countries',
	'storages',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'captcha',
	# Local Apps
	'main',
	'blog',
	'accounts',
	'houses',
	'rooms',
	'bills',
	'utils',
	'dashboard',
	'marketing',
	'emails',
	'payments',
	'garbageday',
	'eggs',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Roomscout.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'accounts', 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'Roomscout.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
	'default': ''
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


try:
	from .local_settings import *
except ImportError:
	pass

if 'test' in sys.argv:
	DATABASES['default'] = {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'testingdb'
	}
